from pathlib import Path

#настраиваем откуда берем и куда кидаем готовое плюс создаем переменные для статистики
BASE_DIR = Path(__file__).resolve().parent
source_dir = BASE_DIR / "cleaned"
normalized_dir = BASE_DIR / "normalized"
normalized_dir.mkdir(exist_ok=True)
total_before = 0 #до
total_after = 0 #после
empty_after = [] #пусто после
#убираем пробелы и убираем дубли
for file_path in source_dir.glob("*.txt"):
    text = file_path.read_text(encoding="utf-8")
    before = len(text)
    
    clean_lines = []
    for line in text.splitlines():
        cleaned = " ".join(line.replace("\u00a0", " ").replace("\t", " ").split())
        if cleaned and cleaned not in clean_lines:
            clean_lines.append(cleaned)
            
    normalized = "\n".join(clean_lines)
    after = len(normalized)

    #пропускаем если после чистки ничего не осталось
    if after == 0:
        empty_after.append(file_path.name)
        continue

    (normalized_dir / file_path.name).write_text(normalized, encoding="utf-8")

    total_before += before
    total_after += after
    print(f"{file_path.name}: {before} - {after}")
#итоговая статистика на сколько все сжалось и были ли пустые
print("---")
print("Всего до:", total_before)
print("Всего после:", total_after)
if total_before > 0:
    percent = (total_before - total_after) / total_before * 100
    print(f"Сокращение: {round(percent, 1)}%")
if empty_after:
    print("пустые после очистки:", empty_after)
else:
    print("пустых документов нет")
print("---")
