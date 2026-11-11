import pandas as pd

df = pd.read_csv('students.csv')
print(df.groupby('Группа')['Баллы'].agg(['mean', 'min', 'max', 'count']))
print(df.groupby('Группа')[['Баллы', 'Посещено']].mean())
print(df.groupby('Группа')['Баллы'].mean().sort_values(ascending=False))
print(df.groupby('Группа')['Баллы'].mean().reset_index())