from pathlib import Path

def clean_line(line):
    line = line.replace("\u00a0", " ")
    line = line.replace("\t", " ")
    line = " ".join(line.split())
    return line

def normalize_text(text):
    lines = text.splitlines()
    clean_lines = []

    for line in lines:
        line = clean_line(line)
        if line == "":
            continue
        if line not in clean_lines:
            clean_lines.append(line)

    return "\n".join(clean_lines)

source_dir = Path("cleaned")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)

files = list(source_dir.glob("*.txt"))

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)

    output_path = normalized_dir / file_path.name
    output_path.write_text(normalized, encoding="utf-8")

    print(file_path.name, len(text), "→", len(normalized))