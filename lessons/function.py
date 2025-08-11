def kvadrat(a, b):
    return (a ** 2) + (2 * a * b) + (b ** 2)


a, b = int(input()), int(input())

print(f'Квадрат суммы {a} и {b} = {kvadrat(a, b)}')

k2 = kvadrat(7, 9)
print(f'другой квадрат = {k2}')

k3 = kvadrat(9, 11)
print(f'k3 = {k3}')

print(f'Разница квадратов {k2} и {k3} = {k2 - k3}')


