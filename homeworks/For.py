# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in numbers:
#     print(i ** 2)

# numbers = list(map(int, input().split()))
# print(sum(numbers))

# numbers = list(map(int, input().split()))
#
# for i in numbers:
#     if i % 2 == 0:

# films = input().split()
#
# for i, film in enumerate(films):
#     print(f'Индекс {i}: {film}')

# fruits = ['яблоко', 'банан', 'вишня']
# for i, fruit in enumerate(fruits):
#     print(f"Итерация {i}: {fruit}")

# Матрица Скала Схватка Бэтман

# films = input().split()
# sum_elem = 0
#
# for i in films:
#     sum_elem += len(i)
#
# print(sum_elem)

# num = 7
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# for i in numbers:
#     print(num * i)

# 1 2 3 4 5 6 7 8 9 10
# numbers = list(map(int, input().split()))
#
# # for i, numb in enumerate(numbers):
# #     if i % 2 == 0:
# #         print(numb)
# # альтернативный вариант через срезы
# for i in numbers[::2]:
#     print(i)

# numbers = list(map(int, input().split()))

# result = 0
# count = 0
#
# if count > 0:
#     for i in numbers:
#         result += i
#         count += 1
#     print(result / count)
# else:
#     print('Деление на ноль')

# Альтернативный и элегантный вариант:
# numbers = list(map(int, input().split()))
# print(sum(numbers) / len(numbers))

# bugi9vugi3
a = input()

for i in a:
    if i.isalpha():
        print(i)
