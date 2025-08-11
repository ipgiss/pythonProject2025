# numbers = list(range(1, 15, 3))
# print(numbers)
#
# print(len(numbers))
# print(numbers[4])

# a = int(input())
#
# for i in range(1, a + 1):
#     print(i ** 2)

# films = input().split()
# # for i in films:
# #     if len(i) >= 5:
# #         print(i)
# count = 0
# for i in films:
#     if len(i) % 2 == 0:
#         count += 1
# print(count)

list_1 = input()
count = 0
#
# for i in list_1:
#     if not (i.isdigit() or i.isalpha() or i.isspace()):
#         count += 1
# print(count)

for i in list_1:
    if i in "0123456789":
        count += 1
print(count)