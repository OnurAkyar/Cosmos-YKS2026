import re
import os

def chunk_by_main_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

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
        first_line = chunk.splitlines()[0]
        title = first_line.lstrip('#').strip()
        safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
        filename = f"{i+1:02d}_{safe_title}.txt"
        filepath = os.path.join(output_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chunk)

        print(f"Written: {filepath}")


def process_all_markdown(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith("-formatted.txt"):
                filepath = os.path.join(dirpath, file)

                print(f"\nProcessing: {filepath}")

                # Create output folder next to the file
                base_name = os.path.splitext(file)[0]
                output_folder = os.path.join(dirpath, f"{base_name}_chunks")

                chunks = chunk_by_main_header(filepath)
                write_chunks_to_folder(chunks, output_folder)

                print(f"Total chunks: {len(chunks)}")


if __name__ == "__main__":
    root_folder = "prepped_textbooks/ayt"
    process_all_markdown(root_folder)