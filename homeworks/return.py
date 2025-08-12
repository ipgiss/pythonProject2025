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
# def new_function():
#     parts = input().strip().split()
#
#     surname = parts[0]
#     name = parts[1][0]
#     ot4 = parts[2][0]
#
#     return f'{surname} {name}.{ot4}.'
#
# print(new_function())

# 6
# Напишите функцию new_function(), которая принимает два значения: строку - это Имя и число - это год рождения. Текущий год по дефолту 2024
# Создайте код который выведет на печать "Меня зовут <Имя>, мне <возраст>."
# def new_function():
#     name = input()
#     year = int(input())
#     current_year = 2024
#
#     age = current_year - year
#     print(f'Меня зовут {name}, мне {age}.')  # Меня зовут <Имя>, мне <возраст>.
#
#
# new_function()

# 7
# Напишите 3 функции: logic(), russia(), england(). Примите два значения в виде строк: первое - Имя, второе - Страна проживания.
# Функция logic() должна их отработать, если страна = Россия, то отрабатывает функция russia() и выводит на печать "Здравствуй <Имя>",
# если страна = England, то отрабатывает функция england() и выводит на печать "Hello <Имя>".

# def logic(name: str, country: str) -> None:
#     if country == 'Россия':
#         russia(name)
#     elif country == 'England':
#         england(name)
#
#
# def russia(name: str) -> None:
#     print(f'Здравствуй {name}')
#
#
# def england(name: str) -> None:
#     print(f'Hello {name}')
#
#
# # Ввод данных
# name = input()
# country = input()
#
# logic(name, country) # запуск функции с двумя переменными

# 7
def russia(name):
    with open('russia.txt', 'w', encoding='utf-8') as f:
        f.write(name)
    with open('russia.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def england(name):
    with open('england.txt', 'w', encoding='utf-8') as f:
        f.write(name)
    with open('england.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def logic(name: str, country: str) -> None:
    if country == 'Россия':
        russia(name)
    elif country == 'England':
        england(name)


user_name = input()
user_country = input()

logic(user_name, user_country)
