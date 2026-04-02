"""
tokenise_and_pack.py
====================
Stage 2 — Tokenisation & sequence packing for CPT.

Reads train.jsonl / val.jsonl produced by md_to_jsonl.py, tokenises with
the Qwen tokeniser, packs documents into fixed-length chunks, and saves
HuggingFace Arrow datasets ready for Trainer.

Usage:
    python tokenise_and_pack.py

Requirements:
    pip install transformers datasets

Output:
    output/
        packed/
            train/          ← HF Arrow dataset (input_ids + labels)
            val/
            packing_stats.json
"""

import json
import os
from pathlib import Path
from itertools import chain
from typing import Generator

from datasets import Dataset, DatasetDict
from transformers import AutoTokenizer

# ── configuration ─────────────────────────────────────────────────────────────

MODEL_NAME      = "Qwen/Qwen2.5-14B"   # change to your exact checkpoint path
                                        # e.g. "/scratch/models/qwen2.5-14b"

INPUT_DIR       = Path("output")        # where train.jsonl / val.jsonl live
OUTPUT_DIR      = Path("output/packed")

MAX_SEQ_LEN     = 4096                  # sequence length fed to the model
                                        # 4096 is a safe default for 12-14B on A100
                                        # raise to 8192 if you have the VRAM

NUM_PROC        = 8                     # parallel workers for tokenisation
                                        # set to number of CPUs available on UHeM node

TEXT_FIELD      = "text"                # field name in your JSONL

# ─────────────────────────────────────────────────────────────────────────────


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def build_tokeniser(model_name: str) -> AutoTokenizer:
    print(f"Loading tokeniser: {model_name}")
    tok = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True,
        use_fast=True,
    )
    # Qwen uses <|endoftext|> as EOS — verify it resolves correctly
    if tok.eos_token is None:
        raise ValueError("Tokeniser has no eos_token — check MODEL_NAME")
    print(f"  eos_token : '{tok.eos_token}' (id={tok.eos_token_id})")
    print(f"  vocab size: {tok.vocab_size}")
    return tok


# ── tokenisation ──────────────────────────────────────────────────────────────

def tokenise_batch(batch: dict, tokeniser: AutoTokenizer) -> dict:
    """
    Tokenise a batch of documents and append EOS after each one.

    We do NOT pad or truncate here — that happens in the packing step.
    The EOS token acts as the document boundary signal during training.
    """
    output_ids = []
    for text in batch[TEXT_FIELD]:
        ids = tokeniser(
            text,
            add_special_tokens=False,   # no BOS — packing handles boundaries
            truncation=False,           # never truncate here; packing handles length
        )["input_ids"]
        ids.append(tokeniser.eos_token_id)  # document boundary
        output_ids.append(ids)
    return {"input_ids": output_ids}


# ── sequence packing ──────────────────────────────────────────────────────────

def pack_token_stream(
    token_stream: Generator[int, None, None],
    max_seq_len: int,
) -> list[dict]:
    """
    Consume a flat stream of token ids and yield fixed-length chunks.

    Each chunk becomes one training example.
    labels = input_ids (standard causal LM objective).
    The last incomplete chunk is dropped to keep all lengths equal.
    """
    buffer = []
    packed = []

    for token_id in token_stream:
        buffer.append(token_id)
        if len(buffer) == max_seq_len:
            packed.append({
                "input_ids": buffer,
                "labels":    buffer.copy(),
            })
            buffer = []

    # Drop the final incomplete chunk — uneven lengths break packing efficiency
    dropped = len(buffer)
    return packed, dropped


def pack_dataset(tokenised_ds: Dataset, max_seq_len: int) -> tuple[Dataset, dict]:
    """
    Flatten all token sequences into one stream and pack into fixed-length chunks.
    """
    print(f"  packing into sequences of {max_seq_len} tokens...")

    # Flatten all input_ids into a single iterator
    def token_stream():
        for ids in tokenised_ds["input_ids"]:
            yield from ids

    packed_records, dropped_tokens = pack_token_stream(token_stream(), max_seq_len)

    total_tokens = sum(len(ids) for ids in tokenised_ds["input_ids"])
    kept_tokens  = len(packed_records) * max_seq_len

    stats = {
        "total_tokens":    total_tokens,
        "kept_tokens":     kept_tokens,
        "dropped_tokens":  dropped_tokens,
        "packed_sequences": len(packed_records),
        "packing_efficiency": round(kept_tokens / total_tokens * 100, 2) if total_tokens else 0,
    }

    return Dataset.from_list(packed_records), stats


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tokeniser = build_tokeniser(MODEL_NAME)

    all_stats = {}

    for split in ("train", "val"):
        jsonl_path = INPUT_DIR / f"{split}.jsonl"
        if not jsonl_path.exists():
            print(f"  skipping {split} — {jsonl_path} not found")
            continue

        print(f"\n── {split} ──────────────────────────────────────────")

        # 1. Load JSONL
        records = load_jsonl(jsonl_path)
        print(f"  loaded {len(records)} records")

        raw_ds = Dataset.from_list(records)

        # 2. Tokenise
        print(f"  tokenising with {NUM_PROC} workers...")
        tokenised_ds = raw_ds.map(
            lambda batch: tokenise_batch(batch, tokeniser),
            batched=True,
            batch_size=256,
            num_proc=NUM_PROC,
            remove_columns=raw_ds.column_names,  # drop all metadata cols
            desc=f"tokenising {split}",
        )

        raw_token_count = sum(len(ids) for ids in tokenised_ds["input_ids"])
        print(f"  total tokens (before packing): {raw_token_count:,}")

        # 3. Pack
        packed_ds, pack_stats = pack_dataset(tokenised_ds, MAX_SEQ_LEN)
        print(f"  packed sequences : {pack_stats['packed_sequences']:,}")
        print(f"  packing efficiency: {pack_stats['packing_efficiency']}%")

        # 4. Save Arrow dataset
        save_path = OUTPUT_DIR / split
        packed_ds.save_to_disk(str(save_path))
        print(f"  saved → {save_path}")

        all_stats[split] = pack_stats

    # 5. Write packing stats
    stats_path = OUTPUT_DIR / "packing_stats.json"
    stats_path.write_text(json.dumps(all_stats, indent=2, ensure_ascii=False))
    print(f"\npacking_stats.json → {stats_path}")
    print("\ndone.")


if __name__ == "__main__":
    main()