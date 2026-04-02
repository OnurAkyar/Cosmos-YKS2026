"""
md_to_jsonl.py
==============
Converts paired .md textbook files into a deduplicated JSONL dataset
ready for CPT tokenisation.

Directory layout expected:
    data/
        kimya/
            kimya_tyt_ogm.md
            kimya_tyt_x.md
        fizik/
            fizik_tyt_ogm.md
            fizik_tyt_x.md
        ...

Output:
    output/
        train.jsonl
        val.jsonl
        stats.json

Each JSONL line:
    {"text": "...", "subject": "kimya", "level": "tyt", "source": "ogm"}

======================================================================
DEDUPLICATION — to disable, set DEDUP_ENABLED = False below.
======================================================================
"""

import json
import re
import random
import hashlib
import unicodedata
from pathlib import Path
from collections import defaultdict

# ── configuration ────────────────────────────────────────────────────────────

DATA_DIR        = Path("data")          # root folder with one subdir per subject
OUTPUT_DIR      = Path("output")
TRAIN_SPLIT     = 0.95                  # 95% train, 5% val
MIN_CHARS       = 150                   # drop sections shorter than this
RANDOM_SEED     = 42

# ── deduplication toggle ──────────────────────────────────────────────────────
DEDUP_ENABLED   = False                  # set False to skip dedup entirely
DEDUP_THRESHOLD = 0.9                   # Jaccard similarity; lower = more aggressive
SHINGLE_SIZE    = 5                     # n-gram size for shingling
# ─────────────────────────────────────────────────────────────────────────────


# ── text helpers ──────────────────────────────────────────────────────────────

def normalise(text: str) -> str:
    """Lowercase + unicode normalise for comparison only (not stored)."""
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_text(text: str, keep_markdown_headings: bool = False) -> str:
    """
    Clean raw markdown text for training.

    keep_markdown_headings=True  → keep '# Heading' syntax (Qwen handles it)
    keep_markdown_headings=False → replace with plain newline separator
    """
    text = unicodedata.normalize("NFC", text)
    if not keep_markdown_headings:
        # Replace '# Heading' with the heading text + blank line
        text = re.sub(r"^#+\s*(.+)$", r"\1\n", text, flags=re.MULTILINE)

    # Collapse 3+ consecutive newlines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text


def split_by_headings(md_text: str) -> list[dict]:
    """
    Split markdown into sections at every H1 ('# ...') boundary.
    Returns list of {'heading': str, 'body': str}.
    """
    pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(md_text))

    sections = []
    for i, match in enumerate(matches):
        heading = match.group(2).strip()
        start   = match.end()
        end     = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body    = md_text[start:end].strip()
        sections.append({"heading": heading, "body": body})

    # Edge case: content before the first heading
    if matches:
        preamble = md_text[: matches[0].start()].strip()
        if preamble:
            sections.insert(0, {"heading": "", "body": preamble})

    return sections


def infer_metadata(filepath: Path) -> dict:
    """
    Extract subject, level, source from filename.
    Expects pattern: {subject}_{level}_{source}.md
    e.g. kimya_tyt_ogm.md → subject=kimya, level=tyt, source=ogm
    """
    parts = filepath.stem.split("_")
    return {
        "subject": parts[0] if len(parts) > 0 else "unknown",
        "level":   parts[1] if len(parts) > 1 else "unknown",
        "source":  parts[2] if len(parts) > 2 else "unknown",
    }


# ── deduplication ─────────────────────────────────────────────────────────────

def shingle(text: str, k: int = SHINGLE_SIZE) -> set[str]:
    """Character-level k-shingles from normalised text."""
    norm = normalise(text)
    if len(norm) < k:
        return {norm}
    return {norm[i: i + k] for i in range(len(norm) - k + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def dedup_pair(records_a: list[dict], records_b: list[dict]) -> list[dict]:
    """
    Given two lists of records from source A and source B for the same subject,
    return the merged list with near-duplicates from B removed.

    Strategy: keep everything from A; for each record in B, drop it if its
    similarity to any record in A exceeds DEDUP_THRESHOLD.
    """
    shingles_a = [shingle(r["text"]) for r in records_a]

    kept_b = []
    dropped = 0
    for rec in records_b:
        sh_b = shingle(rec["text"])
        is_dup = any(
            jaccard(sh_a, sh_b) >= DEDUP_THRESHOLD for sh_a in shingles_a
        )
        if is_dup:
            dropped += 1
        else:
            kept_b.append(rec)

    print(f"    dedup: dropped {dropped}/{len(records_b)} records from source B")
    return records_a + kept_b


# ── main pipeline ─────────────────────────────────────────────────────────────

def process_file(md_path: Path) -> list[dict]:
    """Parse one .md file into a list of training records."""
    meta = infer_metadata(md_path)
    raw  = md_path.read_text(encoding="utf-8")

    sections = split_by_headings(raw)
    records  = []

    for sec in sections:
        # Combine heading + body into one text block
        heading_line = f"{sec['heading']}\n\n" if sec["heading"] else ""
        full_text    = clean_text(heading_line + sec["body"])

        if len(full_text) < MIN_CHARS:
            continue

        records.append({
            "text":    full_text,
            "subject": meta["subject"],
            "level":   meta["level"],
            "source":  meta["source"],
        })

    return records


def build_dataset() -> tuple[list[dict], dict]:
    """Walk DATA_DIR, process all subject folders, return all records + stats."""
    all_records = []
    stats       = {"subjects": {}, "total_before_dedup": 0, "total_after_dedup": 0}

    for subject_dir in sorted(DATA_DIR.iterdir()):
        if not subject_dir.is_dir():
            continue

        md_files = sorted(subject_dir.glob("*.md"))
        if not md_files:
            continue

        subject_name = subject_dir.name
        print(f"\n[{subject_name}]")

        # Group files into pairs (or singles if only one source)
        file_groups: dict[str, list[Path]] = defaultdict(list)
        for f in md_files:
            meta  = infer_metadata(f)
            # group key: subject + level (same curriculum, different sources)
            key   = f"{meta['subject']}_{meta['level']}"
            file_groups[key].append(f)

        subject_records = []
        for key, files in file_groups.items():
            group_records = []
            for f in files:
                recs = process_file(f)
                print(f"  {f.name}: {len(recs)} sections")
                group_records.append(recs)

            if DEDUP_ENABLED and len(group_records) == 2:
                merged = dedup_pair(group_records[0], group_records[1])
            else:
                # flatten without dedup
                merged = [r for recs in group_records for r in recs]

            subject_records.extend(merged)

        stats["subjects"][subject_name] = len(subject_records)
        all_records.extend(subject_records)

    stats["total_after_dedup"] = len(all_records)
    return all_records, stats


def write_splits(records: list[dict], stats: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    random.seed(RANDOM_SEED)
    random.shuffle(records)

    cut        = int(len(records) * TRAIN_SPLIT)
    train_recs = records[:cut]
    val_recs   = records[cut:]

    for split_name, split_recs in [("train", train_recs), ("val", val_recs)]:
        out_path = OUTPUT_DIR / f"{split_name}.jsonl"
        with out_path.open("w", encoding="utf-8") as f:
            for rec in split_recs:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"\n{split_name}.jsonl → {len(split_recs)} records ({out_path})")

    stats["train_records"] = len(train_recs)
    stats["val_records"]   = len(val_recs)
    stats["dedup_enabled"] = DEDUP_ENABLED

    stats_path = OUTPUT_DIR / "stats.json"
    stats_path.write_text(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"stats.json  → {stats_path}")


# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== md_to_jsonl conversion ===")
    print(f"dedup: {'enabled (threshold={})'.format(DEDUP_THRESHOLD) if DEDUP_ENABLED else 'DISABLED'}")

    records, stats = build_dataset()

    print(f"\ntotal records: {stats['total_after_dedup']}")
    write_splits(records, stats)
    print("\ndone.")