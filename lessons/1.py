class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
        return f'val = {self.val}'


a = CountFromBy()  # запуск Класса

a.increase()
print(a)
a.increase(5, 12)
print(a)
