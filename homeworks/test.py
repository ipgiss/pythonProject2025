def logic(name: str, country: str) -> None:
    if country == 'Россия':
        russia(name)
    elif country == 'England':
        england(name)


def russia(name):
    print(f'Здравствуй {name}')


def england(name):
    print(f'Hello {name}')


user_name = input()
user_country = input()

logic(user_name, user_country)
