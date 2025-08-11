# def description(name, age, sex):
#     print(f'Имя {name}, возраст {age}, пол {sex}')
#
# # description('Anna', 30, 'f') # позиционный аргумент
# description(name='Anna', age=30, sex='f') #именованный аргумент
# description(sex='m', age=25, name='Vasya') # можно менять местами аргументы, но при выводе будет позиции, как они стоят в функции.


# name_2 = input('Введите ваше имя: ')
# age_2 = input('Введите ваш возраст ')
#
# def description(name, age, sex):
#     print(f'Имя {name}, возраст {age}, пол {sex}')
#
# description(name_2, age_2, 'f')

# def sum_numbers():
#     num_1 = int(input())
#     num_2 = int(input())
#     print(num_1 + num_2)
#
# sum_numbers()
#
# def sum_return(a, b):
#     return a + b
#
# result = sum_return(5, 12)
# print(result)

import random

user = 'User_'
# number = random.randrange(1, 1000)
# name = user + str(number)
# print(name)

# or

name = f'User__{random.randrange(1, 100)}'
print(name)