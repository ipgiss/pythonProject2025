'''4.6. Задание по Классам'''


class Car:
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        print(
            f'Машина {self.model}, {self.year} года выпуска, объем двигателя {self.engine} см3, цена на текущий год {self.price}уе, текущий пробег {self.mileage} км и у нее {self.wheels} колеса :)')


car1 = Car('ford Bronco', 2018, 3200, 25000, 125000)
car1.description()


class Truck(Car):
    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.wheels = 8

    def description(self):
        '''Переопределяем метод Родителя'''
        print(
            f'Грузовик фирмы {self.model}, год выпуска {self.year}, двигатель {self.engine} см3, цена {self.year}уе, пробег на сегодня {self.mileage} км. Внимание, в грузовике {self.wheels} колсес! \nОбращайтесь только в провереный шиномонтаж :)')


truck1 = Truck('Scania', 2020, 15000, 50000, 70000)
truck1.description()
