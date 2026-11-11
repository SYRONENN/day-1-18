import pandas as pd

df = pd.read_csv("students.csv")
df_sort1 = df.sort_values("Баллы")
print(df_sort1)
df_sort2 = df.sort_values("Баллы", ascending=False)
print(df_sort2)

df_sort3 = df.sort_values(["Группа", "Баллы"], ascending=[True, False])
print(df_sort3)
df["Пропущено"] = 20 - df["Посещено"]
df["Процент"] = (df["Посещено"] / 20 * 100).round(1)
df["Баллы+5"] = df["Баллы"] + 5
print(df)