class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def __repr__(self) -> str:  # Представление результата в виде строки
        return str(self.val)

    def __str__(self) -> str:
        return f'{self.val}'

    def increase(self) -> None:  # self - первый параметр любого метода(фунции) в Классе.
        self.val += self.incr  # Берем из объекта текущее значение val и увеличиваем его на значение incr


# Создаём объект
a = CountFromBy()
print(a)
a.increase()  # Увеличиваем val на incr
print(a)
a.increase()  # Увеличиваем еще val на incr
print(a)

b = CountFromBy()
for _ in range(10):
    b.increase()
print(f'b = {b}')
