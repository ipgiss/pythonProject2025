# my_dict = {
#     "name": "Алиса",
#     "age": 25,
#     "city": "Москва"
# }
#
# # print(my_dict['ahe'])
# print(my_dict.get('job', ' not here')) # безопасный вариант, если опечатка или если нет ключа такого

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'b': 3, 'c': 4}

# merged = dict_1 | dict_2
# print(merged)

dict_1.update(dict_2)
print(dict_1)