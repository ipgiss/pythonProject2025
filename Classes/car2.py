class Car:
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        wheel = 4

    def description(self):
        print(
            f'Машина {self.model}, произведена в {self.year} году, '
            f'двигатель {self.engine} см3, цена {self.price} руб, '
            f'пробег {self.mileage} км.')


car1 = Car('Nissan X-trail', 2013, 2000, 1300000, 155000)
car1.description()
print(car1.mileage)
