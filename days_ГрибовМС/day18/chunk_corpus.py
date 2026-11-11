from pathlib import Path
import csv

def split_with_overlap(text, chunk_size, overlap, minimum_length=30):
    chunks = []
    step = chunk_size - overlap
    
    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()
        
        if len(chunk) >= minimum_length:
            chunks.append(chunk)
            
    return chunks
source_dir = Path("normalized")
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)
files = list(source_dir.glob("*.txt"))
all_chunks = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    
    chunks = split_with_overlap(text, 250, 50)
    
    for chunk_id, chunk in enumerate(chunks):
        filename = f"{file_path.stem}_chunk_{chunk_id}.txt"
        output_path = chunks_dir / filename
        output_path.write_text(chunk, encoding="utf-8")

        row = [file_path.name, chunk_id, len(chunk)]
        all_chunks.append(row)

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    writer.writerows(all_chunks)

print("Документов:", len(files))
print("Всего чанков:", len(all_chunks))