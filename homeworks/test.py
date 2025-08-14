var = input()
string_list = ['10', '20', 'abc']

try:
    index = int(var)
    element = string_list[index]
    number = int(element)
    print('Good')
except ValueError:
    print('Bad')
except IndexError:
    print('Bad')
