import pandas as pd

df = pd.read_csv("students.csv")
df = df.rename(columns={"Баллы": "Тестовый балл"})
df.to_csv("all_students_result.csv", index=False, encoding="utf-8")

df_high = df[df["Тестовый балл"] >= 80]
df_high.to_csv("high_scores.csv", index=False, encoding="utf-8")
df26 = pd.read_csv("students.csv")
res27 = df26[(df26["Баллы"] >= 80) & (df26["Посещено"] >= 16)]
res28 = df26.sort_values("Баллы", ascending=False)
df26.to_csv("result.csv", index=False)