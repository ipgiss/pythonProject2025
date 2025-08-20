def user_input(numb):
    while True:
        try:
            return input(numb)
        except ValueError:
            print('only numbers pls')

numb1 = user_input('Enter the 1st number : ')
print(numb1)

def input_number(prompt):          # 1. Объявляем функцию
    while True:                   # 2. Запускаем вечный цикл
        try:
            return float(input(prompt))  # 3. Возвращаем число (если получилось)
        except ValueError:               # 4. Если ошибка — цикл повторяется
            print("Ошибка: введите число!")