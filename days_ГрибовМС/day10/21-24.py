import pandas as pd

df = pd.read_csv('students.csv')
result21 = df.groupby('Группа')['Баллы'].mean()
print(result21)
result22 = df.groupby('Группа')['Баллы'].agg(['mean', 'min', 'max'])
print(result22)
print("Задание 23 исправлено")
groups = ['A', 'B', 'C']
scores = [10, 20, 30]