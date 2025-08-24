class Person:
    '''Модель человека'''

    def __init__(self, name, age):  # инициализация + список обязательный параметров
        self.name = name
        self.age = age
        print('Персона создана')

    def sing(self):
        print(f'{self.name} может спеть!')

    def dance(self):
        print(f'{self.name} может танцевать!')


# создадим Объект, т.е. экземпляр Класса
man = Person('Vasya', 25)
# print(man.name)
woman = Person('Anya', 28)

man.dance()
woman.sing()