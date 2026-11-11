import pandas as pd

df = pd.read_csv("students.csv")

df["Пропущено"] = 20 - df["Посещено"]
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)

result = df[(df["Баллы"] >= 70) & (df["Посещено"] >= 16)]
result = result.sort_values("Баллы", ascending=False)

print(result)
result.to_csv("result.csv", index=False, encoding="utf-8")