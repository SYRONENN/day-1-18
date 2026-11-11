text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chunk_size = 10

chunks = []

for start in range(0, len(text), chunk_size):
    chunk = text[start:start + chunk_size]
    chunks.append(chunk)

print(chunks)