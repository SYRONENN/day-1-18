import pandas as pd

df = pd.read_csv('students.csv')

df.groupby('Группа')['Баллы'].mean().to_csv('average_by_group.csv')
df.groupby('Группа')['Посещено'].mean().to_csv('average_by_group2.csv')