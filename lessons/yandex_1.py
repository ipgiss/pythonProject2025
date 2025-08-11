num = int(input())

# a = num // 10
# b = num % 10
#
# print(a)
# print(b)

# 3х-значное число
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
#
# print(a)
# print(b)
# print(c)

# попробую 4х-значное разложить
# a = num // 1000
# b = (num % 1000) // 100
# c = (num % 100) // 10
# d = num % 10
#
# print(a)
# print(b)
# print(c)
# print(d)

# 5-digit
# a = num // 10000
# b = (num % 10000) // 1000
# c = (num % 1000) // 100
# d = (num % 100) // 10
# e = num % 10
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# когда много чисел есть два варианта
# digits = []
# num = 12345
# while num > 0:
#     digits.insert(0, num % 10)
#     num //= 10
# print(digits)  # [1, 2, 3, 4, 5] выводит Список

# вариант 2, с append() и потом reverse() — будет быстрее при больших числах.
# digits = []
# num = int(input())
# while num > 0:
#     digits.append(num % 10)
#     num //= 10
#
# digits.reverse()  # Переворачиваем список, чтобы был в нужном порядке
#
# print(digits)
