"""
DeepSeek-OCR-2 PDF Parser
=========================
Parses a PDF file page-by-page using DeepSeek-OCR-2 (Transformers inference).
Each page is converted to an image via PyMuPDF (fitz) -- no poppler needed.

Key differences from OCR-1:
  - Model: deepseek-ai/DeepSeek-OCR-2
  - image_size: 768 (was 640)
  - Dynamic resolution: (0-6)x768x768 + 1x1024x1024
  - Better accuracy on complex layouts

Requirements:
    pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
    pip install transformers==4.46.3 tokenizers==0.20.3
    pip install PyMuPDF Pillow numpy einops easydict addict huggingface_hub hf_xet

Usage:
    python deepseek_ocr2_pdf_parser.py --pdf example.pdf --output ocr_output --mode markdown --pages 9 20
    python deepseek_ocr2_pdf_parser.py --retry-empty
"""

import os
import sys
import json
import glob
import types
import argparse
import importlib.util
import torch

# Enable fastest available attention kernels (free, built into PyTorch 2.x)
torch.backends.cuda.enable_flash_sdp(True)
torch.backends.cuda.enable_mem_efficient_sdp(True)
torch.backends.cuda.enable_math_sdp(False)

import fitz
fitz.TOOLS.mupdf_display_errors(False)

from PIL import Image


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_PDF    = "tyt-turkce-ogm-1-20.pdf"
DEFAULT_OUTPUT = "ocr_output"
MODEL_NAME     = "deepseek-ai/DeepSeek-OCR-2"

PROMPTS = {
    "free":     "<image>\nFree OCR. ",
    "markdown": "<image>\n<|grounding|>Convert the document to markdown. ",
}

# OCR-2 uses image_size=768 instead of 640
DEFAULT_BASE_SIZE  = 1024
DEFAULT_IMAGE_SIZE = 768

# Retry strategies: (label, crop_mode, base_size, image_size, dpi)
RETRY_STRATEGIES = [
    ("default",    True,  1024, 768, 200),
    ("no-crop",    False, 1024, 768, 200),
    ("small-tile", True,  768,  512, 200),
    ("low-res",    True,  1024, 768, 150),
]


# ---------------------------------------------------------------------------
# Register snapshot as a package so relative imports work
# ---------------------------------------------------------------------------

def load_snapshot_as_package(model_dir: str, package_name: str = "deepseek_ocr2_pkg"):
    if package_name in sys.modules:
        return sys.modules[package_name]

    pkg = types.ModuleType(package_name)
    pkg.__path__    = [model_dir]
    pkg.__package__ = package_name
    pkg.__file__    = os.path.join(model_dir, "__init__.py")
    sys.modules[package_name] = pkg

    for fname in sorted(os.listdir(model_dir)):
        if not fname.endswith(".py"):
            continue
        mod_name  = fname[:-3]
        full_name = f"{package_name}.{mod_name}"
        fpath     = os.path.join(model_dir, fname)
        spec      = importlib.util.spec_from_file_location(
                        full_name, fpath, submodule_search_locations=[])
        module             = importlib.util.module_from_spec(spec)
        module.__package__ = package_name
        sys.modules[full_name] = module
        try:
            spec.loader.exec_module(module)
            setattr(pkg, mod_name, module)
        except ImportError as e:
            # Auto-install missing packages required by model files
            missing = str(e).replace("No module named '", "").replace("'", "").split(".")[0]
            print(f"[INFO] Auto-installing missing package: {missing}")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", missing, "-q"])
            try:
                spec2   = importlib.util.spec_from_file_location(
                              full_name, fpath, submodule_search_locations=[])
                module2             = importlib.util.module_from_spec(spec2)
                module2.__package__ = package_name
                sys.modules[full_name] = module2
                spec2.loader.exec_module(module2)
                setattr(pkg, mod_name, module2)
            except Exception as e2:
                if full_name in sys.modules:
                    del sys.modules[full_name]
                print(f"[DEBUG] Skipped {fname} after install: {e2}")
        except Exception as e:
            if full_name in sys.modules:
                del sys.modules[full_name]
            print(f"[DEBUG] Skipped {fname}: {e}")

    return pkg


def find_ocr_class(pkg):
    import inspect
    for attr_name in dir(pkg):
        module = getattr(pkg, attr_name, None)
        if not isinstance(module, types.ModuleType):
            continue
        for cls_name, cls in inspect.getmembers(module, inspect.isclass):
            if hasattr(cls, "infer") and hasattr(cls, "from_pretrained"):
                print(f"[INFO] Found OCR class : {cls_name}  (in {attr_name}.py)")
                return cls
    return None


# ---------------------------------------------------------------------------
# Model loader
# ---------------------------------------------------------------------------

_model     = None
_tokenizer = None
_device    = None


def load_model(model_name: str = MODEL_NAME):
    global _model, _tokenizer, _device

    if _model is not None:
        return _model, _tokenizer

    _device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype   = torch.bfloat16 if _device == "cuda" else torch.float32

    print(f"[INFO] Loading model : {model_name}")
    print(f"[INFO] Device        : {_device.upper()}  |  dtype: {dtype}")

    from huggingface_hub import snapshot_download
    from transformers import AutoTokenizer

    model_dir = snapshot_download(repo_id=model_name)
    print(f"[INFO] Snapshot      : {model_dir}")

    # List all .py files found in snapshot for debugging
    py_files = [f for f in os.listdir(model_dir) if f.endswith(".py")]
    print(f"[INFO] Python files  : {py_files}")

    pkg        = load_snapshot_as_package(model_dir, "deepseek_ocr2_pkg")
    _tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    ModelClass = find_ocr_class(pkg)

    if ModelClass is not None:
        print(f"[INFO] Loading with  : {ModelClass.__name__}.from_pretrained()")
        _model = ModelClass.from_pretrained(
            model_dir,
            torch_dtype=dtype,
            trust_remote_code=True,
        )
    else:
        # Direct import fallback: load modeling_deepseekocr2.py by file path
        print("[WARN] Package scan failed -- trying direct file import.")
        import importlib.util as _ilu
        ocr2_path = os.path.join(model_dir, "modeling_deepseekocr2.py")
        if os.path.exists(ocr2_path):
            spec   = _ilu.spec_from_file_location("modeling_deepseekocr2", ocr2_path)
            mod    = _ilu.module_from_spec(spec)
            mod.__package__ = "deepseek_ocr2_pkg"
            sys.modules["modeling_deepseekocr2"] = mod
            sys.modules["deepseek_ocr2_pkg.modeling_deepseekocr2"] = mod
            spec.loader.exec_module(mod)
            # find class with infer()
            import inspect as _inspect
            for cname, cls in _inspect.getmembers(mod, _inspect.isclass):
                if hasattr(cls, "infer") and hasattr(cls, "from_pretrained"):
                    ModelClass = cls
                    print(f"[INFO] Direct import found: {cname}")
                    break

        if ModelClass is not None:
            _model = ModelClass.from_pretrained(
                model_dir, torch_dtype=dtype, trust_remote_code=True,
            )
        else:
            print("[WARN] Falling back to AutoModel (type mismatch warning is harmless).")
            from transformers import AutoModel
            _model = AutoModel.from_pretrained(
                model_dir,
                _attn_implementation="eager",
                trust_remote_code=True,
                use_safetensors=True,
                torch_dtype=dtype,
            )

    _model = _model.eval().to(_device)

    # torch.compile: ~20% speedup after first page warm-up
    try:
        _model = torch.compile(_model, mode="reduce-overhead")
        print("[INFO] torch.compile  : enabled (first page will be slower).")
    except Exception as e:
        print(f"[WARN] torch.compile skipped: {e}")

    print(f"[INFO] Model ready on {_device.upper()}.\n")
    return _model, _tokenizer


# ---------------------------------------------------------------------------
# PDF -> PIL Images
# ---------------------------------------------------------------------------

def pdf_to_images(pdf_path: str, dpi: int = 200, page_range=None):
    print(f"[INFO] Opening PDF : {pdf_path}")
    doc   = fitz.open(pdf_path)
    total = len(doc)
    print(f"[INFO] Total pages : {total}")

    if page_range:
        first = max(1, page_range[0]) - 1
        last  = min(total, page_range[1]) - 1
    else:
        first, last = 0, total - 1

    zoom   = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    pages = []
    for idx in range(first, last + 1):
        page = doc[idx]
        pix  = page.get_pixmap(matrix=matrix, colorspace=fitz.csRGB)
        img  = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        pages.append((idx + 1, img))
        print(f"[INFO]   Rendered page {idx + 1}  ({pix.width}x{pix.height} px)")

    doc.close()
    print(f"[INFO] {len(pages)} page(s) ready.\n")
    return pages


def render_single_page(pdf_path: str, page_num: int, dpi: int = 200) -> Image.Image:
    doc    = fitz.open(pdf_path)
    page   = doc[page_num - 1]
    zoom   = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    pix    = page.get_pixmap(matrix=matrix, colorspace=fitz.csRGB)
    img    = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()
    return img


# ---------------------------------------------------------------------------
# .mmd reader
# ---------------------------------------------------------------------------

def read_mmd_output(output_path: str, img_stem: str) -> str:
    exact = os.path.join(output_path, f"{img_stem}.mmd")
    if os.path.exists(exact):
        with open(exact, encoding="utf-8") as f:
            return f.read().strip()

    mmd_files = sorted(glob.glob(os.path.join(output_path, "*.mmd")),
                       key=os.path.getmtime, reverse=True)
    if mmd_files:
        with open(mmd_files[0], encoding="utf-8") as f:
            return f.read().strip()
    return ""


# ---------------------------------------------------------------------------
# Single inference call
# ---------------------------------------------------------------------------

def run_infer(
    image: Image.Image,
    output_path: str,
    prompt: str,
    img_stem: str,
    base_size: int  = DEFAULT_BASE_SIZE,
    image_size: int = DEFAULT_IMAGE_SIZE,
    crop_mode: bool = True,
) -> str:
    model, tokenizer = load_model()

    tmp_img_path = os.path.join(output_path, f"{img_stem}.png")
    image.save(tmp_img_path, format="PNG")

    try:
        result = model.infer(
            tokenizer,
            prompt=prompt,
            image_file=tmp_img_path,
            output_path=output_path,
            base_size=base_size,
            image_size=image_size,
            crop_mode=crop_mode,
            save_results=True,
            test_compress=True,
        )
    except torch.cuda.OutOfMemoryError:
        print(f"\n[WARN] CUDA OOM -- clearing cache.")
        torch.cuda.empty_cache()
        return ""
    except Exception as exc:
        print(f"\n[WARN] infer() raised: {exc}")
        return ""
    finally:
        if os.path.exists(tmp_img_path):
            os.remove(tmp_img_path)

    # Try return value first, then fall back to .mmd file
    text = ""
    if result is not None:
        if isinstance(result, dict):
            text = result.get("text", result.get("output", ""))
        elif isinstance(result, str):
            text = result.strip()

    if not text:
        text = read_mmd_output(output_path, img_stem)

    return text


# ---------------------------------------------------------------------------
# Split-page strategy
# ---------------------------------------------------------------------------

def ocr_split_halves(
    image: Image.Image,
    output_path: str,
    prompt: str,
    page_num: int,
) -> str:
    w, h   = image.size
    top    = image.crop((0, 0, w, h // 2))
    bottom = image.crop((0, h // 2, w, h))

    top_dir = os.path.join(output_path, "split_top")
    bot_dir = os.path.join(output_path, "split_bottom")
    os.makedirs(top_dir, exist_ok=True)
    os.makedirs(bot_dir, exist_ok=True)

    print(f"\n         [split] top half ...", end=" ", flush=True)
    top_text = run_infer(top, top_dir, prompt, f"page_{page_num:04d}_top")
    print(f"{'OK' if top_text else 'empty'}")

    print(f"         [split] bottom half ...", end=" ", flush=True)
    bot_text = run_infer(bottom, bot_dir, prompt, f"page_{page_num:04d}_bottom")
    print(f"{'OK' if bot_text else 'empty'}")

    return "\n\n".join(t for t in [top_text, bot_text] if t)


# ---------------------------------------------------------------------------
# OCR one page with retries
# ---------------------------------------------------------------------------

def ocr_page_with_retry(
    image: Image.Image,
    output_path: str,
    prompt: str,
    page_num: int,
    pdf_path: str,
) -> tuple:
    for label, crop_mode, base_size, image_size, dpi in RETRY_STRATEGIES:
        print(f"\n         [strategy: {label}] ...", end=" ", flush=True)

        img  = render_single_page(pdf_path, page_num, dpi=dpi) if dpi != 200 else image
        stem = f"page_{page_num:04d}_{label}"
        text = run_infer(img, output_path, prompt, stem,
                         base_size, image_size, crop_mode)

        if text:
            print(f"OK  ({len(text)} chars)")
            return text, label

        print("empty -- trying next strategy")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # Last resort: split halves
    print(f"\n         [strategy: split-halves] ...", end=" ", flush=True)
    text = ocr_split_halves(image, output_path, prompt, page_num)
    return (text, "split-halves") if text else ("", "all-failed")


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def parse_pdf(
    pdf_path: str,
    output_dir: str,
    mode: str = "markdown",
    dpi: int = 200,
    page_range=None,
    retry_empty: bool = False,
):
    pdf_path   = os.path.abspath(pdf_path)
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    prompt = PROMPTS.get(mode, PROMPTS["markdown"])
    print(f"[INFO] OCR mode : '{mode}'")
    print(f"[INFO] Prompt   : {prompt!r}")
    print(f"[INFO] Model    : {MODEL_NAME}\n")

    # --retry-empty: only reprocess pages with empty .txt files
    if retry_empty:
        page_images = []
        for page_dir in sorted(glob.glob(os.path.join(output_dir, "page_*"))):
            page_num = int(os.path.basename(page_dir).split("_")[1])
            txt_file = os.path.join(page_dir, f"page_{page_num:04d}.txt")
            if os.path.exists(txt_file):
                content = open(txt_file, encoding="utf-8").read().strip()
                if not content:
                    img = render_single_page(pdf_path, page_num, dpi=dpi)
                    page_images.append((page_num, img))
                    print(f"[INFO] Queued empty page {page_num} for retry.")
        if not page_images:
            print("[INFO] No empty pages found.")
            return {}
    else:
        page_images = pdf_to_images(pdf_path, dpi=dpi, page_range=page_range)

    total_pages     = len(page_images)
    results         = {}
    strategies_used = {}

    for i, (page_num, image) in enumerate(page_images, 1):
        page_out_dir = os.path.join(output_dir, f"page_{page_num:04d}")
        os.makedirs(page_out_dir, exist_ok=True)

        print(f"[{i}/{total_pages}] OCR page {page_num} ...", end=" ", flush=True)

        try:
            stem = f"page_{page_num:04d}_default"
            text = run_infer(image, page_out_dir, prompt, stem)

            if text:
                strategy = "default"
                print(f"OK  ({len(text)} chars)  |  {text[:60].replace(chr(10),' ')!r}")
            else:
                print("empty -- retrying ...")
                text, strategy = ocr_page_with_retry(
                    image, page_out_dir, prompt, page_num, pdf_path
                )

            results[page_num]         = text
            strategies_used[page_num] = strategy

            txt_file = os.path.join(page_out_dir, f"page_{page_num:04d}.txt")
            with open(txt_file, "w", encoding="utf-8") as f:
                f.write(text)

            if not text:
                print(f"         [WARN] Page {page_num} empty after all strategies.")

        except Exception as exc:
            import traceback
            print(f"\n[ERROR] Page {page_num}: {exc}")
            traceback.print_exc()
            results[page_num]         = f"[ERROR: {exc}]"
            strategies_used[page_num] = "error"

        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # Save combined outputs
    combined_txt  = os.path.join(output_dir, "full_text.txt")
    combined_mmd  = os.path.join(output_dir, "full_text.mmd")
    combined_json = os.path.join(output_dir, "full_text.json")

    with open(combined_txt, "w", encoding="utf-8") as f:
        for p in sorted(results):
            f.write(f"\n{'='*60}\nPAGE {p}  [strategy: {strategies_used.get(p,'?')}]\n{'='*60}\n\n")
            f.write(results[p])
            f.write("\n")

    with open(combined_mmd, "w", encoding="utf-8") as f:
        for p in sorted(results):
            f.write(f"\n<!-- PAGE {p} -->\n\n")
            f.write(results[p])
            f.write("\n")

    with open(combined_json, "w", encoding="utf-8") as f:
        json.dump(
            {str(k): {"text": v, "strategy": strategies_used.get(k, "?")}
             for k, v in sorted(results.items())},
            f, ensure_ascii=False, indent=2,
        )

    empty_pages  = [p for p, t in results.items() if not t or t.startswith("[ERROR")]
    filled_pages = [p for p, t in results.items() if t and not t.startswith("[ERROR")]

    print(f"\n{'='*60}")
    print(f"[INFO] SUMMARY")
    print(f"{'='*60}")
    print(f"  Model            : {MODEL_NAME}")
    print(f"  Successful pages : {filled_pages}")
    print(f"  Empty/failed     : {empty_pages}")
    print(f"  Strategies used  : {strategies_used}")
    print(f"  Combined text    : {combined_txt}")
    print(f"  Combined mmd     : {combined_mmd}")
    print(f"  Combined json    : {combined_json}")
    if empty_pages:
        print(f"\n  Tip: re-run with --retry-empty to attempt failed pages again.")
    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Parse a PDF with DeepSeek-OCR-2 -- Windows friendly, no poppler."
    )
    parser.add_argument("--pdf",         default=DEFAULT_PDF)
    parser.add_argument("--output",      default=DEFAULT_OUTPUT)
    parser.add_argument("--mode",        choices=list(PROMPTS.keys()), default="markdown")
    parser.add_argument("--pages",       nargs=2, type=int,
                        metavar=("FIRST", "LAST"), default=None)
    parser.add_argument("--dpi",         type=int, default=200)
    parser.add_argument("--retry-empty", action="store_true",
                        help="Retry only pages that previously had empty output")
    return parser.parse_args()


if __name__ == "__main__":
    args       = parse_args()
    page_range = tuple(args.pages) if args.pages else None

    parse_pdf(
        pdf_path    = args.pdf,
        output_dir  = args.output,
        mode        = args.mode,
        dpi         = args.dpi,
        page_range  = page_range,
        retry_empty = args.retry_empty,
    )
