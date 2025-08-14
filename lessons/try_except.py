# import math
#
#
# def circutArea(radius):
#     return math.pi * radius ** 2
#
#
# while True:
#     try:
#         r = int(input('Введите радиус: '))
#         # if r > 0:
#         break
#         # else:
#         #     print('Введите число больше 0')
#     except Exception as e:
#         print(f'Произошла ошибка {e}')
#
# area = circutArea(r)
# print(f'Площадь круга = {area:.2f}')

try:
    a = int(input())
    b = int(input())
    result = a / b
except(ZeroDivisionError, ValueError) as er:
    print(er)
else:
    print(f'Результат деления = {result}')

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Нужно вводить только числа!')
