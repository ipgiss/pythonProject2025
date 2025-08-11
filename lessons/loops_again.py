# как "пробегаться" по Списку циклами:
# 1. Простой цикл for (самый частый способ)

fruits = ['яблоко', 'банан', 'апельсин']

for f in fruits:
    print(f)

# 2. Цикл с доступом к индексам через enumerate()
for index, f in enumerate(fruits, start=1):
    print(f'Индекс: {index}, Фрукт: {f}')  # Индекс: 1, Фрукт: яблоко и тд.

colors = ['красный', 'зелёный', 'синий']
for i, color in enumerate(colors):
    print(f"Цвет №{i + 1}: {color}")
