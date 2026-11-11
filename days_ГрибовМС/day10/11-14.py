import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y)
plt.show()
categories = ['1ИИ-1', '1ИИ-2', 'Другая']
values = [78.3, 81.0, 50.0]
plt.bar(categories, values)
plt.title('График')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.grid(True)
plt.show()