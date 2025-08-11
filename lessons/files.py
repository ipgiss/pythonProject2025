# file = open('test.txt', 'w')
# file.write('Hello, world!')
# file.close()

# with open('test.txt', 'r') as file:
#     for line in file:      # читает файл построчно
#         print(line.strip())  # strip() удаляет переносы строк

# file = open('test.txt', 'w')
# # file.write('Новая строка \n Потом еще строка\n и еще одна')
# file.close()

# file = open('test.txt', 'r') # чтение файла
# content = file.read()
# print(content)

# with open('test.txt', 'w') as file:
#     file.write('Обновим данные \n')

# several = ["First line\n", "Second line\n", "Third line\n"]
# with open('test.txt', 'w') as file:
#     file.writelines(several)

# with open('test.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# with open('test.txt', 'w') as file:
#     file.write('This will be appended\n')

# with open('test.txt', 'r') as file:
#     content = file.read()
# print(content)

# # чтение и дозапись
# with open('test.txt', 'a+', encoding='windows-1251') as file:
#     file.write('Новая строка еще одна c win-1251 \n')
#     file.seek(0)
#     content = file.read()
# print(content)

# import pandas as pd
# from pathlib import Path
#
# path = Path(r"C:\Users\k.kuznetsov\PycharmProjects\pythonProject2025\lessons\test.txt")
#
# try:
#     # Пробуем стандартную кодировку (utf-8)
#     text = pd.read_csv(path, header=None)
#     print("Успешно прочитано с utf-8:")
#     print(text.head(5))
#
# except UnicodeDecodeError:
#     try:
#         # Пробуем windows-1251 для русских файлов
#         text = pd.read_csv(path, header=None, encoding='windows-1251')
#         print("Успешно прочитано с windows-1251:")
#         print(text.head(5))
#
#     except Exception as e:
#         print(f"Ошибка при чтении файла: {e}")
#         print("Попробуйте другие кодировки: cp1252, iso-8859-1, latin1")

# import os
# print("Текущая рабочая папка:", os.getcwd())  # Куда смотрит Python?
# print("Файлы в папке:", os.listdir())  # Видит ли 'test.txt'?
#
# path = 'C:\Users\k.kuznetsov\PycharmProjects\pythonProject2025\lessons'


# import pandas as pd
# from pathlib import Path
#
# path = Path(r"C:\Users\k.kuznetsov\PycharmProjects\pythonProject2025\lessons\test.txt")

# try:
#     # Пробуем сначала без указания кодировки (PyCharm часто сам определяет)
#     df = pd.read_csv(path, header=None)
#     print("Успешно! Первые строки:")
#     print(df.head())
#
# except UnicodeDecodeError:
#     # Если ошибка кодировки, пробуем windows-1251 (для русских Windows)
#     try:
#         df = pd.read_csv(path, header=None, encoding='windows-1251')
#         print("Успешно с кодировкой windows-1251! Первые строки:")
#         print(df.head())
#     except Exception as e:
#         print(f"Ошибка при чтении с windows-1251: {e}")
#
# except Exception as e:
#     print(f"Другая ошибка: {e}")


# Вариант с try/except - нужен только для обработки возможных ошибок.
# import pandas as pd
# from pathlib import Path
#
# # Указываем путь к файлу
# path = Path(r"C:\Users\k.kuznetsov\PycharmProjects\pythonProject2025\lessons\test.txt")
#
# # Читаем файл с явным указанием кодировки windows-1251
# try:
#     text = pd.read_csv(path, header=None, encoding='windows-1251')
#     print("Файл успешно прочитан в кодировке windows-1251:")
#     print(text.head(5))
# except Exception as e:
#     print(f"Ошибка при чтении файла: {e}")

# Вариант без try\except:
# import pandas as pd
# from pathlib import Path
# #
# path = Path(r"C:\Users\k.kuznetsov\PycharmProjects\pythonProject2025\lessons\test.txt")
# # text = pd.read_csv(path, header=None, encoding='windows-1251')
# # print(text.head(5))

# def smart_read_csv(path, encodings=('windows-1251', 'utf-8', 'cp866')):
#     for enc in encodings:
#         try:
#             return pd.read_csv(path, encoding=enc)
#         except UnicodeDecodeError:
#             continue
#     raise ValueError(f"Не удалось прочитать файл {path} с кодировками: {encodings}")
#
# # # Использование
# text = smart_read_csv(path)
# print(text.head())
