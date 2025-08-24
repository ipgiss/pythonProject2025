#1 Определяем Класс (чертеж)
class Car:

    # Конструктор --init--. Тут мы задаем начальные хар-ки машин
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0
        self.fuel_level = 100

    # Методы (действия, которые машина может выполнять) - это функции внутри Класса.
    # Первый параметр ВСЕГДА `self` - так метод получает доступ к конкретному объекту (машине), над которым выполняется действие

    def start_engine(self):
        print(f'{self.model}: Двигатель заведен! Вруммм')


# 4 Создаем Объекты (вне Класса)
my_tesla = Car('Tesla Model S', 'white', 250)

# 5. Вызов объектов через точку (.)
print('---Моя Тесла---')
my_tesla.start_engine() # Вызов метода для объекта my_tesla

# 6. Получаем доступ к Аттрибутам объекта тоже через точку (.)
print(f'Макс скорость Теслы: {my_tesla.max_speed} км\ч')