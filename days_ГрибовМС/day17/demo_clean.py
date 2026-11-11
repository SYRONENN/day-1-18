dirty = """Список — упорядоченная коллекция элементов.


Создаётся с помощью квадратных скобок []


Элементы разделяются запятыми


Можно изменять, добавлять и удалять элементы


Индексация начинается с нуля
Метод append() добавляет элемент в конец списка
"""

print("до:")
print(repr(dirty))
print()
clean_lines = []
for line in dirty.splitlines():
    cleaned = " ".join(line.replace("\u00a0", " ").replace("\t", " ").split())
    if cleaned and cleaned not in clean_lines:
        clean_lines.append(cleaned)

clean = "\n".join(clean_lines)
print("после:")
print(clean)
print()
before = len(dirty)
after = len(clean)
removed = before - after
print("---")
print("До:", before)
print("После:", after)
print("Удалено:", removed)
print("---")
if before > 0:
    percent = removed / before * 100
    print(f"Сокращение: {round(percent, 1)}%")