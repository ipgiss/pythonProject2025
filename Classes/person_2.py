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
man.description()
man2.description()
man.update_weight(90)
man.get_weight()


'''Изучаю Наследование'''
class Warrior(Person2):
    '''Создаем класс Warrior как Наследник класса Person'''

    def __init__(self, name, age, height):
        super().__init__(name, age, height)

