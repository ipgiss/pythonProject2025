# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# # c = set1.union(set2)
# # print(c)
#
# # объединение
# print(set1 | set2)
#
# # пересечение
# print(set1 & set2) # 3
#
# # разность
# print(set1 - set2) # 1, 2

# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
#
# common = numbers_1 & numbers_2
#
# for i in sorted(common):
#     print(i)

# valid_users = frozenset(["user1", "user2"])
# access_rules = {valid_users: 'admin'}
#
# input_users = {"user2", "user1"}
#
# if frozenset(input_users) in access_rules:
#     print('Access Granted')

# access_rules = {
#     frozenset(["admin", "root"]): "superuser",
#     frozenset(["editor", "writer"]): "content_team",
#     frozenset(["guest"]): "read_only"
# }
#
#
# def check_access(user_roles: set):
#     for group, access in access_rules.items():
#         if user_roles & group:
#             return f'Доступ: {access}'
#     return 'Доступ запрещен'
#
#
# print(check_access({'admin'}))
# print(check_access({'guest'}))


# def greet(name: str) -> None:
#     if not isinstance(name, str):
#         raise TypeError('Ожидается строка')
#     print(f'Привет, {name}!')
#
#
# input_name = input('Введите ваше имя: ')
# greet(input_name)

# def greet_2 (name: str):
#     print(f'Привет, {name}!')
#
# greet_2(1235)

# def greet_2(name: str):
#     if not isinstance(name, str):  # Явная проверка типа
#         raise TypeError("Только строки!")
#     print(f"Привет, {name}!")
#
#
# greet_2(124)

# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
#
# if numbers_1 & numbers_2:
#     print('GOOD')
# else:
#     print('Bad')


# join_numb = numbers_1 | numbers_2
#
# for i in sorted(join_numb):
#     print(i)


numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

# common = numbers_1 & numbers_2 & numbers_3
# if common: # Если в common есть элементы
#     print('Good')
# else:
#     print('Bad')

common_1_2 = numbers_1 & numbers_2 # элементы, есть и в numbers_1, и в numbers_2
result = common_1_2 - numbers_3 # вычитаем элементы numbers_3

print(result)

