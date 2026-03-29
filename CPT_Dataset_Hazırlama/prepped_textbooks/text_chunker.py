import re
import os

def chunk_by_main_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split on lines that start with exactly one '#' (not '##', '###', etc.)
    parts = re.split(r'(?=\n# (?!#))', content)

    chunks = []
    for part in parts:
        part = part.strip()
        if part:
            chunks.append(part)

    return chunks


def write_chunks_to_folder(chunks, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for i, chunk in enumerate(chunks):
        # Derive a filename from the # header line
        first_line = chunk.splitlines()[0]
        title = first_line.lstrip('#').strip()
        safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
        filename = f"{i+1:02d}_{safe_title}.txt"
        filepath = os.path.join(output_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chunk)

        print(f"Written: {filename}")


if __name__ == "__main__":
    filepath = r"ayt-tarih-formatted.md"
    output_folder = "ayt-tarih-chunks"

    chunks = chunk_by_main_header(filepath)
    write_chunks_to_folder(chunks, output_folder)

    print(f"\nTotal chunks written: {len(chunks)}")