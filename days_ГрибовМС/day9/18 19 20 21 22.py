import pandas as pd

df_miss = pd.read_csv("students_missing.csv")
print(df_miss.isna())
print(df_miss.isna().sum())
df_not_na = df_miss[df_miss["Баллы"].notna()]
print(df_not_na)
srednee = df_miss["Баллы"].mean()
df_miss["Баллы"] = df_miss["Баллы"].fillna(srednee)
print(df_miss)

df_clean = df_miss.dropna().reset_index(drop=True)
print(df_clean)