class Person2:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def calories(self):
        return self.weight /2

man = Person2('Vasya', 25, 100)

print(man.calories())