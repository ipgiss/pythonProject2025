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
# def russia(name):
#     with open('russia.txt', 'w', encoding='utf-8') as f:
#         f.write(name)
#     with open('russia.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#
# def england(name):
#     with open('england.txt', 'w', encoding='utf-8') as f:
#         f.write(name)
#     with open('england.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#
# def logic(name: str, country: str) -> None:
#     if country == 'Россия':
#         russia(name)
#     elif country == 'England':
#         england(name)
#
#
# user_name = input()
# user_country = input()
#
# logic(user_name, user_country)

# 8
'''Напишите функцию new_function(), которая принимает два значения в виде чисел. Первое - количество дней и оно может быть от 1 до 3,
в противном случае выводит Bad. Второе - баланс на счете, не может быть меньше 30, в противном случае выводим Bad.
Функция new_function() создает файл file.txt, затем производит списывание 7 рублей за каждый день и записывает в файл построчно строки,
за каждый день списывания, по формату, далее вывести на печать содержимое файла:
<Нумерация дня> день - баланс <Баланс> - списалось 7 - осталось <Баланс - Нумерация дня * 7>'''

# def new_function():
#     days = int(input())  # от 1 до 3
#     balance = int(input())  # не меньше 30
#
#     # проверка условий задачи
#     if days < 1 or days > 3 or balance < 30:
#         print('Bad')
#         return  # Выходим из функции, если условие не выполнено
#
#     with open('file.txt', 'w', encoding='utf-8') as f:
#         for day in range(1, days + 1):  # Цикл по дням (1, 2, 3)
#             # if balance < 7:
#             #     break
#             remain = balance - 7
#             # Формируем строку для каждого дня
#             line = f'{day} день - баланс {balance} - списалось 7 - осталось {remain}\n'
#             f.write(line)
#             balance = remain  # меняем исходную переменную баланса
#
#     with open('file.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#
# new_function()
#
# # <Нумерация дня> день - баланс <Баланс> - списалось 7 - осталось <Баланс - Нумерация дня * 7>
# # 1 день - баланс 100 - списалось 7 - осталось 93


# 9
'''Напишите функцию new_function(), которая принимает два значения в виде чисел. Первое - баланс на карте. Второе - сумма перевода.
Если сумма перевод меньше баланса, то производи перевод и выводим на печать остаток на балансе.
Если сумма перевода больше баланса, то выводим на печать "Не хватает денежных средств".
Если суммы равны, то выводим "0"'''

# def new_function():
#     try:  # приучаю себе всегда добавлять try-except при вводе.
#         balance = int(input())
#         transfer = int(input())
#     except ValueError:
#         print('Ошибка - введите число!')
#         return
#
#     if transfer < balance:
#         print(balance - transfer)
#     elif transfer > balance:
#         print('Не хватает денежных средств')
#     else:
#         print('0')
#
#
# new_function()

# 10
'''Напишите функцию new_function(), которая принимает два значения в виде чисел. Свадебный банкет, первое число - количество гостей,
 которые будут есть, второе число - количество гостей которые будут пить чай. Второе число не может быть больше первого, иначе выводим Bad.
Стоимость еды на одного человека - 3000
Стоимость чая на одного человека - 500
Произвести расчет суммы стоимости свадебно банкета из количества кушающих и пьющих чай гостей.'''


def new_function():
    try:  # просто тренируюсь с try-except руку набить ))
        guest_eat = int(input())
        guest_drink = int(input())
    except ValueError:
        print('Введите только число!')

    if guest_drink > guest_eat:
        print('Bad')
        return

    eat = 3000
    drink = 500

    sum_total = guest_eat * eat + guest_drink * drink
    print(sum_total)


new_function()

# данный блок закончен!