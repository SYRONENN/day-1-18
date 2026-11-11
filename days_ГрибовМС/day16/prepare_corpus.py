from pathlib import Path

#функция убирает пустые строки и лишние пробелы по краям
def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)
    return "\n".join(clean_lines)


BASE_DIR = Path(__file__).resolve().parent
corpus_dir = BASE_DIR / "corpus"
cleaned_dir = BASE_DIR / "cleaned"
cleaned_dir.mkdir(exist_ok=True)
files = list(corpus_dir.rglob("*.txt"))

#читаем файлы чистим и сохраняем в новую папку
documents = []
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    text = clean_text(text)

    if text == "":
        print("Пропущен пустой файл:", file_path.name)
        continue
    documents.append({
        "source": file_path.name,
        "text": text
    })
    output_path = cleaned_dir / file_path.name
    output_path.write_text(text, encoding="utf-8")
# количество документов и длину каждого
print("Документов:", len(documents))
for document in documents:
    print(document["source"], len(document["text"]))
