from pathlib import Path

#функция для очистки текста от пустых строк и пробелов
def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)
    return "\n".join(clean_lines)
#откуда брать и куда сохранять
BASE_DIR = Path(__file__).resolve().parent
corpus_dir = BASE_DIR / "corpus"
cleaned_dir = BASE_DIR / "cleaned"
cleaned_dir.mkdir(exist_ok=True)

#ищем все тхт файлы и создаем список под них
files = list(corpus_dir.glob("*.txt"))
documents = []
#проходимся по каждому файлу чистим и сохраняем
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    source = file_path.name

    text = clean_text(text)

    if text == "":
        print("Пропущен пустой документ:", source)
        continue

    document = {
        "source": source,
        "text": text
    }
    documents.append(document)
    output_path = cleaned_dir / source
    output_path.write_text(text, encoding="utf-8")
print("Документов в корпусе:", len(documents))
#считаем сколько символов в каждом файле и всего
total_chars = 0
for doc in documents:
    length = len(doc["text"])
    total_chars += length
    print(f"{doc['source']}: {length} символов")

    if length < 50:
        print(f"  Предупреждение: короткий документ {doc['source']}")
print("Всего символов в корпусе:", total_chars)