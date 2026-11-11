import pandas as pd

df = pd.read_csv("students.csv")
print(df["Имя"])
print(df[["Имя", "Баллы"]])
print(df[["Имя", "Группа", "Посещено"]])

res7 = df[df["Баллы"] >= 80]
print(res7)
res8 = df[df["Группа"] == "1ИИ-2"]
print(res8)
res9 = df[df["Посещено"] < 16]
print(res9)
res10 = df[(df["Баллы"] >= 75) & (df["Посещено"] >= 16)]
print(res10)
res11 = df[(df["Баллы"] >= 90) | (df["Посещено"] == 20)]
print(res11)