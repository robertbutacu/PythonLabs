'''1. Sa se scrie o functie care primeste ca parametri doua liste a si b
    si returneaza un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a)
'''

def ex1(a, b):
    intersection = map(lambda x: x in b, a)
    reunion = set(a + b)
    a_minus_b = map(lambda x: x not in b, a)
    b_minus_a = map(lambda x: x not in a, b)

    return intersection, reunion, a_minus_b, b_minus_a

