# CPT Dataset Preparation

This directory contains tools and utilities for preparing Cosmos-YKS2026 CPT datasets through PDF parsing and text processing.

### 📝 `prepped_textbooks/`
Pre-processed and formatted textbook data ready for use.
- **Structure:**
  - `text_chunker.py` - Utility for splitting large texts into manageable chunks
  - Subject folders (e.g., `biyoloji-tyt-ogm/`) containing:
    - `*-formatted.txt` - Clean, formatted full text
    - `*-parsed.txt` - Parsed and structured text
    - `*-chunks/` - Subdivided content by topic

### Choosing a Parser
- **Default choice:** Use `Marker` for speed and efficiency
- **Special case:** Use `DeepSeek` only when PDFs contain important images with embedded text

### Manual Formatting
- Post-processing is usually handled via LLM prompting for quality. Automation would be ideal, but the variance in extracted text makes it difficult.