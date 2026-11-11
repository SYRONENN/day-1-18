import pandas as pd
import tkinter as tk
df = pd.read_csv('students.csv')
res25 = df.groupby('Группа')['Баллы'].agg(['mean', 'min', 'max', 'count']).reset_index()
print(res25)
res25.to_csv('average_by_group.csv', index=False)
root = tk.Tk()
root.title("Задание 25")
root.mainloop()
