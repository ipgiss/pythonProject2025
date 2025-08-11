# new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}
#
# for key, value in new_dict.items():
#     if value > 100:
#         print(key)

# 2

# 3
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
#
# new_dict = dict1 | dict2
# print(new_dict)
#
# for key, value in new_dict.items():
#     print(f'{key} - {value}')

# dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'a': 25}
# print(dict3)
# # dict3['a'] = 15
# # print(dict3)

# Через множества
# words = ['hello', 'world', 'hello']
# unique_words = set(words)  # ['world', 'hello']
# print(unique_words)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
#
# for key, value in dict1.items():
#     print(f"{value} - {key}")  # Просто меняем value и key местами в выводе


# countries = {'Россия': 'Москва', 'Франция': 'Париж'}
#
# for country, capital in countries.items():
#     print(f'Столицей {country} является {capital}')

# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
#
# common = numbers_2 & numbers_1
# 
# for i in sorted(common):
#     print(i)
