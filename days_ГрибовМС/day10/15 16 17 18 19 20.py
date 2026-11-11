import pandas as pd
import tkinter as tk
df = pd.read_csv('students.csv')
gr = df.groupby('Группа')['Баллы'].mean().reset_index()

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg='white')
canvas.pack()
canvas.create_rectangle(50, 200 - gr.loc[0, 'Баллы']*2, 100, 200, fill='blue')
canvas.create_text(75, 10, text=gr.loc[0, 'Группа'])
canvas.create_rectangle(150, 200 - gr.loc[1, 'Баллы']*2, 200, 200, fill='blue')
canvas.create_text(175, 10, text=gr.loc[1, 'Группа'])
root.mainloop()