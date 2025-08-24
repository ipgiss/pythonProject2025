# # import csv
# #
# # part_list = []
# # with open('storage_list.csv', 'r', encoding='utf-8-sig') as file:
# #     reader = csv.reader(file)
# #     for row in reader:
# #         if row:
# #             part_list.append(row[0].strip())
# #
# # print(part_list)  # Выведет ВЕСЬ список (все ~200 номеров)
# # print(f"Всего номеров: {len(part_list)}")  # print(part_list[:5]) выводит первые 5 для проверки
#
# # import pandas as pd
# #
# # part_list = pd.read_csv('storage_list.csv', header=None, encoding='utf-8-sig')[0].tolist()
# # print(part_list)  # Весь список
# # print(f"Всего номеров: {len(part_list)}")  # print(part_list[:5]) выводит первые 5 для проверки
#
# # BOM (\ufeff) добавляется некоторыми программами (например, Excel при сохранении в UTF-8)
# # Обычный utf-8 не удаляет этот маркер, а utf-8-sig обрабатывает его корректно
#
# # import pandas as pd
# #
# # # Загружаем данные
# # df = pd.read_csv('storage_list.csv', header=None, encoding='utf-8-sig')
# #
# # # Переименуем столбец для удобства (если нужно)
# # df.columns = ['Part_Number']
# #
# # # Проверяем первые 5 строк
# # print("Первые 5 номеров:")
# # print(df.head())
# #
# # # Проверяем последние 5 строк
# # print("\nПоследние 5 номеров:")
# # print(df.tail())
# #
# # # Альтернативно: можно указать количество строк (например, 10)
# # print("\nПервые 10 номеров:")
# # print(df.head(10))
#
import pandas as pd
#
# Задание 1 (если есть заголовок 'Part_Number')
df = pd.read_csv('storage_list.csv', header=None, encoding='utf-8-sig')
a_end = df[df[0].str.endswith('A')]  # Фильтр по первому столбцу
print(a_end.head())
# print()
# print(df.columns)
# a_end.to_csv('new_csv.csv', index=None)

# Задание 3 (длина и дефис)
long_numbers = df[df[0].str.len() > 10]
print(f'длинных названий = {len(long_numbers)}')
# hyphen_numbers = df[df['Part_Number'].str.contains('-')]