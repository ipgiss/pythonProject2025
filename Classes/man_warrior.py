# импортируем сразу два Класса в один файл

from base_person import Person2, Warrior # либо "звездочку" * поставить, чтобы не перечислять все Классы.

man2 = Person2('Vasya', 20, 180)
warrior2 = Warrior('Fighter', 32, 210)

man2.description()
print(warrior2.description()) # тут return был, поэтому через print

