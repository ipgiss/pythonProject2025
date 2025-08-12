import math


def circle_area(radius):
    return math.pi * radius ** 2


while True:
    try:
        r = int(input('Введите радиус: '))
        break
    except ValueError:
        print('Введите только число!')

area = circle_area(r)
print(f'Площадь круга = {area:.2f}')

# теперь надо добавить try-except

