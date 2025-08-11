while True:
    age_input = input('Введите ваш возраст: ')
    if not age_input.isdigit():
        print('Введите число!')
        continue

    age = int(age_input)
    break

print(f'Ваш возраст {age} лет!')
