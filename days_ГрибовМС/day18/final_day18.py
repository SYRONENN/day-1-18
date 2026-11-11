from pathlib import Path
import csv

#функция длелит текст на чанки
def split_with_overlap(text, chunk_size, overlap, minimum_length=30):
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()
        if len(chunk) >= minimum_length:
            chunks.append(chunk)

    return chunks
# задаем папки откуда брать текст и куда кидать чанки
BASE_DIR = Path(__file__).parent
source_dir = BASE_DIR / "normalized"
chunks_dir = BASE_DIR / "chunks"
chunks_dir.mkdir(exist_ok=True)
files = list(source_dir.glob("*.txt"))
all_chunks = []

#делим на чанки и каждый в отдельный файл
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    chunks = split_with_overlap(text, 250, 50)

    for chunk_id, chunk in enumerate(chunks):
        filename = f"{file_path.stem}_chunk_{chunk_id}.txt"
        output_path = chunks_dir / filename
        output_path.write_text(chunk, encoding="utf-8")
        row = [file_path.name, chunk_id, len(chunk)]
        all_chunks.append(row)

#пишем сводку по всем чанкам в цсв таблицу
with open(BASE_DIR / "chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    writer.writerows(all_chunks)
#выводим общую статистику и среднюю длину куска
print("Документов:", len(files))
print("Всего чанков:", len(all_chunks))

if len(all_chunks) > 0:
    total_length = 0
    for row in all_chunks:
        total_length += row[2]
    average = total_length / len(all_chunks)
    print("Средняя длина:", round(average, 1))
