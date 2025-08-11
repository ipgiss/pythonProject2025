# with open('test2.txt', 'w') as file:
#     file.write('First line \n')
#
# with open('test2.txt', 'a') as file:
#     file.write('Second line \n')
#
# with open('test2.txt', 'a+') as file:
#     file.write('third line \n')
#     file.seek(0)
#     content = file.read()
# print(content)

# Читаем первую строку
# with open('test2.txt', 'r') as file:
#     first_line = file.readline()
#     second_line = file.readline()  # читает следующую строку
# print(first_line)
# print(second_line)

# with open('test2.txt', 'r') as file:
#     content = file.read()
# print(content)

# 1
# value_1 = input()
#
# with open('file.txt', 'w+') as file:
#     file.write(value_1)
#     file.seek(0)
#     content = file.read()
# print(content)

numbers = list(map(int, input().split()))

with open('file.txt', 'w') as file:
    for numb in numbers:
        file.write(f'{numb}\n')

result = 0
with open('file.txt') as file:
    for i in file:
        result += int(i)
print(result)

# numbers = list(map(int, input().split()))
#
# # Запись в file_1.txt
# with open('file_1.txt', 'w') as f1:
#     for num in numbers:
#         f1.write(f"{num}\n")
#
# # Чтение file_1.txt и запись нечетных строк в file_2.txt
# with open('file_1.txt', 'r') as f1, open('file_2.txt', 'w') as f2:
#     lines = f1.readlines()  # Читаем все строки
#
#     odd_lines = []
#     for i, line in enumerate(lines):
#         if i % 2 == 0:  # Индексы 0, 2, 4 и т.д. (что соответствует 1-й, 3-й, 5-й строкам)
#             odd_lines.append(line)
#
#     f2.writelines(odd_lines)  # Записываем отобранные строки
#
# # Вывод результата
# with open('file_2.txt', 'r') as f2:
#     print("Содержимое file_2.txt:")
#     print(f2.read(), end='')  # end='' убирает лишний перенос строки


