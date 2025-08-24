class Person2:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100  # если заводим постоянное значение, то из init убираем weight.

    def calories(self):
        print(f'Для вас, {self.name}, оптимальный вес = {self.height / 100} кг')

    def description(self):
        print(f'Человека зовут {self.name}, возраст {self.age} лет, рост {self.height} см и вес {self.weight} кг')

    def get_weight(self):
        print(f'Вес человека = {self.weight} кг.')

    def update_weight(self, kg):
        self.weight = kg


man = Person2('Vasya', 25, 170)
man2 = Person2('Olya', 31, 160)

# man.calories()
# man.description()
# man2.description()
# man.update_weight(90)
# man.get_weight()


'''Изучаю Наследование'''


class Warrior(Person2):
    '''Создаем класс Warrior как Наследник класса Person'''

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        '''Получениея значения "ярость" для героя'''
        print(f'Заряд ярости героя = {self.rage}')

    def description(self):
        '''Переопределяем метод Родителя'''
        description = f'Человека зовут {self.name}, возраст {self.age} лет, его ярость {self.rage}'
        # print(description)
        return description

warrior_1 = Warrior('Canon', 30, 200)

warrior_1.update_weight(150)
print(warrior_1.description()) # вызов функции если в ней return
# warrior_1.get_rage()
