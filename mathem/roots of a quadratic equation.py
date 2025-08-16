import math

while True:
    try:
        a, b, c = int(input()), int(input()), int(input())
        break
    except ValueError:
        print('Введите только числа! Попробуйте еще раз')

# дискриминант D=b**2−4ac
D = b ** 2 - 4 * a * c
print(f'Дискриминант = {D}')

if D < 0:
    print('нет действительных корней ')
elif D == 0:
    x = -b / 2 * a
    print(f'Корень при D = 0 равен {int(x)}')
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'Корень x1 = {int(x1)}')
    print(f'Корень x2 = {int(x2)}')
