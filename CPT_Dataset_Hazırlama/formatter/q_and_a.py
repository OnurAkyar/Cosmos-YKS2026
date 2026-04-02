"""
md_to_jsonl.py
==============
Converts paired .md textbook files into a deduplicated JSONL dataset
ready for CPT tokenisation. Incorporates "Mixed Training" LLM augmentation
to generate in-line training QAs and separate evaluation QAs.

Directory layout expected:
    data/
        kimya/
            kimya_tyt_ogm.md
            kimya_tyt_x.md
        fizik/ ...

Output:
    output/
        train.jsonl     (Contains Augmented Text + Mixed Training QAs)
        val.jsonl       (Contains Augmented Text + Mixed Training QAs)
        eval_qa.jsonl   (Contains separate evaluation QA pairs for benchmarking)
        stats.json
"""

import os
import json
import re
import random
import hashlib
import unicodedata
from pathlib import Path
from collections import defaultdict
from openai import OpenAI

# ── configuration ────────────────────────────────────────────────────────────

DATA_DIR        = Path("data")          
OUTPUT_DIR      = Path("output")
TRAIN_SPLIT     = 0.95                  
MIN_CHARS       = 150                   
RANDOM_SEED     = 42

# ── deduplication toggle ──────────────────────────────────────────────────────
DEDUP_ENABLED   = False                  
DEDUP_THRESHOLD = 0.9                   
SHINGLE_SIZE    = 5                     

# ── llm augmentation toggle ───────────────────────────────────────────────────
LLM_AUGMENTATION_ENABLED = True
# Fallback to env variable if not hardcoded here
OPENAI_API_KEY  = os.environ.get("OPENAI_API_KEY", "your-api-key-here")
# Change BASE_URL if you are running Qwen locally via vLLM/Ollama (e.g. "http://localhost:8000/v1")
OPENAI_BASE_URL = None 
LLM_MODEL_NAME  = "qwen-3.5-9b" # or "qwen-3.5-9b" if running locally    "gpt-4o-mini"
 
if LLM_AUGMENTATION_ENABLED:
    client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)

SYSTEM_PROMPT = """
Sen uzman bir eğitim bilimleri ve veri bilimi asistanısın. 
Sana verilen lise ders kitabı metni parçası için şu üç görevi yerine getirmelisin:
1. 'augmented_text': Metni anlamını ve bilgi bütünlüğünü bozmadan farklı bir cümle yapısıyla (paraphrase) yeniden yaz.
2. 'training_qa': Sadece metne dayalı 1 veya 2 adet kolay soru-cevap çifti oluştur.
3. 'eval_qa': Metindeki daha detaylı veya kavramsal bir bilgiye dayalı 1 adet zorlayıcı soru-cevap çifti oluştur.

Çıktını SADECE aşağıdaki JSON formatında ver. Başka hiçbir açıklama ekleme:
{
  "augmented_text": "...",
  "training_qa": [{"Q": "...", "A": "..."}],
  "eval_qa": [{"Q": "...", "A": "..."}]
}
"""
# ─────────────────────────────────────────────────────────────────────────────

# ── text helpers ──────────────────────────────────────────────────────────────

def normalise(text: str) -> str:
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"\s+", " ", text).strip()
    return text

def clean_text(text: str, keep_markdown_headings: bool = False) -> str:
    text = unicodedata.normalize("NFC", text)
    if not keep_markdown_headings:
        text = re.sub(r"^#+\s*(.+)$", r"\1\n", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def split_by_headings(md_text: str) -> list[dict]:
    pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(md_text))

    sections = []
    for i, match in enumerate(matches):
        heading = match.group(2).strip()
        start   = match.end()
        end     = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body    = md_text[start:end].strip()
        sections.append({"heading": heading, "body": body})

    if matches:
        preamble = md_text[: matches[0].start()].strip()
        if preamble:
            sections.insert(0, {"heading": "", "body": preamble})
    elif md_text.strip():
        # If no headings exist at all
        sections.append({"heading": "", "body": md_text.strip()})

    return sections

def infer_metadata(filepath: Path) -> dict:
    parts = filepath.stem.split("_")
    return {
        "subject": parts[0] if len(parts) > 0 else "unknown",
        "level":   parts[1] if len(parts) > 1 else "unknown",
        "source":  parts[2] if len(parts) > 2 else "unknown",
    }


# ── deduplication ─────────────────────────────────────────────────────────────

def shingle(text: str, k: int = SHINGLE_SIZE) -> set[str]:
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
    shingles_a = [shingle(r["text"]) for r in records_a]
    kept_b = []
    dropped = 0
    for rec in records_b:
        sh_b = shingle(rec["text"])
        is_dup = any(jaccard(sh_a, sh_b) >= DEDUP_THRESHOLD for sh_a in shingles_a)
        if is_dup:
            dropped += 1
        else:
            kept_b.append(rec)

    print(f"    dedup: dropped {dropped}/{len(records_b)} records from source B")
    return records_a + kept_b


# ── main pipeline ─────────────────────────────────────────────────────────────

def process_file(md_path: Path) -> list[dict]:
    meta = infer_metadata(md_path)
    raw  = md_path.read_text(encoding="utf-8")

    sections = split_by_headings(raw)
    records  = []

    for sec in sections:
        heading_line = f"{sec['heading']}\n\n" if sec["heading"] else ""
        full_text    = clean_text(heading_line + sec["body"])

        if len(full_text) < MIN_CHARS:
            continue

        records.append({
            "text":    full_text,
            "subject": meta["subject"],
            "level":   meta["level"],
            "source":  meta["source"],
            "eval_qas": [] # Placeholder for LLM phase
        })

    return records


def build_dataset() -> tuple[list[dict], dict]:
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

        file_groups: dict[str, list[Path]] = defaultdict(list)
        for f in md_files:
            meta  = infer_metadata(f)
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
                merged = [r for recs in group_records for r in recs]

            subject_records.extend(merged)

        stats["subjects"][subject_name] = len(subject_records)
        all_records.extend(subject_records)

    stats["total_after_dedup"] = len(all_records)
    return all_records, stats

# ── llm augmentation step ─────────────────────────────────────────────────────

def augment_chunk_with_llm(chunk_text: str) -> dict:
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Metin Parçası:\n{chunk_text}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        # Fallback if API fails: return original text and empty QA lists
        print(f"\n      LLM Error: {e}")
        return {"augmented_text": chunk_text, "training_qa": [], "eval_qa": []}

def run_llm_augmentation(records: list[dict]) -> list[dict]:
    if not LLM_AUGMENTATION_ENABLED:
        return records
        
    print(f"\n=== Running LLM Augmentation on {len(records)} deduplicated records ===")
    
    for i, rec in enumerate(records):
        print(f"  Augmenting record {i+1}/{len(records)}...", end="\r")
        
        llm_data = augment_chunk_with_llm(rec["text"])
        
        # 1. Format the Mixed Training Text
        mixed_text = llm_data.get("augmented_text", rec["text"])
        for qa in llm_data.get("training_qa", []):
            mixed_text += f"\n\nSoru: {qa.get('Q', '')}\nCevap: {qa.get('A', '')}"
            
        # 2. Update the record
        rec["text"] = mixed_text
        rec["eval_qas"] = llm_data.get("eval_qa", [])
        
    print("\nLLM Augmentation complete.")
    return records

# ── file writer ───────────────────────────────────────────────────────────────

def write_splits(records: list[dict], stats: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    random.seed(RANDOM_SEED)
    random.shuffle(records)

    cut        = int(len(records) * TRAIN_SPLIT)
    train_recs = records[:cut]
    val_recs   = records[cut:]
    
    eval_qa_path = OUTPUT_DIR / "eval_qa.jsonl"
    
    with eval_qa_path.open("w", encoding="utf-8") as f_eval:
        for split_name, split_recs in [("train", train_recs), ("val", val_recs)]:
            out_path = OUTPUT_DIR / f"{split_name}.jsonl"
            
            with out_path.open("w", encoding="utf-8") as f_out:
                for rec in split_recs:
                    # Write CPT Record
                    cpt_record = {
                        "text": rec["text"],
                        "subject": rec["subject"],
                        "level": rec["level"],
                        "source": rec["source"]
                    }
                    f_out.write(json.dumps(cpt_record, ensure_ascii=False) + "\n")
                    
                    # Write separate Eval QAs
                    for qa in rec.get("eval_qas", []):
                        eval_record = {
                            "question": qa.get("Q", ""),
                            "answer": qa.get("A", ""),
                            "subject": rec["subject"],
                            "level": rec["level"]
                        }
                        f_eval.write(json.dumps(eval_record, ensure_ascii=False) + "\n")
                        
            print(f"\n{split_name}.jsonl → {len(split_recs)} records ({out_path})")

    print(f"eval_qa.jsonl → Evaluation QAs extracted successfully ({eval_qa_path})")

    stats["train_records"] = len(train_recs)
    stats["val_records"]   = len(val_recs)
    stats["dedup_enabled"] = DEDUP_ENABLED
    stats["llm_augmented"] = LLM_AUGMENTATION_ENABLED

    stats_path = OUTPUT_DIR / "stats.json"
    stats_path.write_text(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"stats.json  → {stats_path}")


# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== md_to_jsonl conversion with CPT Augmentation ===")
    print(f"dedup: {'enabled (threshold={})'.format(DEDUP_THRESHOLD) if DEDUP_ENABLED else 'DISABLED'}")
    print(f"llm  : {'enabled' if LLM_AUGMENTATION_ENABLED else 'DISABLED'}")

    records, stats = build_dataset()
    print(f"\ntotal records after dedup: {stats['total_after_dedup']}")
    
    # Run the LLM augmentation on the deduplicated records
    records = run_llm_augmentation(records)
    
    write_splits(records, stats)
    print("\ndone.")