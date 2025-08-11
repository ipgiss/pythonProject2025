# word = input('Введите букву для поиска: ')
# fruits = ['яблоко', 'банан', 'вишня']
#
# count = 0
#
# for i in fruits:
#     if word in i:
#         print(f'В слове <{i}> есть буква {word}')
#         count += 1
# print(f"Количество элементов которые содержат букву 'б': {count}")

numb = [1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 15, 19, 21, 22, 25]

sum_elem = 0

for i in numb:
    sum_elem += i
print(sum_elem)
