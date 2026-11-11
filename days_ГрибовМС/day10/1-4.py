import pandas as pd

df = pd.read_csv('students.csv')
print(df.groupby('Группа')['Баллы'].mean())
print(df.groupby('Группа')['Баллы'].min())
print(df.groupby('Группа')['Баллы'].max())
print(df.groupby('Группа')['Баллы'].count())