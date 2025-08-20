class Car:

    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    # Методы, т.е. действия, которые машина может выполнять

    def start_engine(self):
        print(f'{self.model}: Двигатель заведен!')


# создаем Объекты
my_tesla = Car('Tesla model S', 'white', 250)

# Вызов метода (функции)
my_tesla.start_engine()