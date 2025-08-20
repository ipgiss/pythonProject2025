class Car:

    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

    # Методы, т.е. действия, которые машина может выполнять

    def start_engine(self):
        print(f'{self.model}: Двигатель заведен!')

    def accelerate(self, amount):
        if self.current_speed + amount <= self.max_speed:
            self.current_speed += amount
        else:
            self.current_speed = self.max_speed
            print(f'{self.model}: Достигнута максимальная скорость ({self.max_speed} км\ч)!')


# создаем Объекты
my_tesla = Car('Tesla model S', 'white', 250)

# Вызов метода (функции)
my_tesla.start_engine()
my_tesla.accelerate(80)
my_tesla.accelerate(200)
