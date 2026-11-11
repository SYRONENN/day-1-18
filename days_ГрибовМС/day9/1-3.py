import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()