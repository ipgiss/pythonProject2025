# def new_function():
#     x = int(input())
#     if x > 6:
#         return 'Bad'
#     elif 1 <= x <= 3:
#         return 'Два' if x == 2 else 'Bad'
#     elif 4 <= x <= 6:
#         return 'Пять' if x == 5 else 'Bad'
#
#
# print(new_function())

# 2
# def new_function():
#     x = int(input())
#     y = 7
#
#     if x % y == 0:
#         return 'Good'
#     else:
#         return 'Bad'
#
#
# print(new_function())

# 3
# def logic():
#     x = int(input())
#     if x % 2 == 0:
#         even(x)
#     else:
#         odd(x)
#
#
# def even(num):
#     print('ЧЕТ')
#
#
# def odd(num):
#     print('НЕЧЕТ')
#
#
# logic()

# 4
# def new_function() -> str:
#     stroka = input().split()
#     return stroka[1]
#
#
# print(new_function())

# 5
def new_function():
    parts = input().strip().split()

    surname = parts[0]
    name = parts[1][0]
    ot4 = parts[2][0]

    return f'{surname} {name}.{ot4}.'

print(new_function())
