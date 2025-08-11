while True:
    try:
        numb = int(input("Введите число от 1 до 100: "))

        if numb > 100 or numb < 1:
            print('Вы ввели некорректное число, попробуйте еще раз')
        elif numb % 2 == 0:
            print('Число четное')
            break
        else:
            print('Число нечетное')
            break

    except ValueError:
        print('Ошибка! Нужно ввести целое число, а не текст.')
