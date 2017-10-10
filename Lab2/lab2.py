import re

import itertools


def is_prime(input):
    return all(map(lambda x: input % x != 0, list(range(2, input // 2))))


'''
Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.
'''


def primes(input):
    return list(filter(lambda x: is_prime(x), input))


print("1. " + str(primes(list(range(0, 100)))))

'''
Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: 
(a intersectat cu b, a reunit cu b, a - b, b - a)
'''


def list_ops(a, b):
    intersection = list(filter(lambda x: x in b, a))
    reunion = set(a + b)
    a_minus_b = list(filter(lambda x: x not in b, a))
    b_minus_a = list(filter(lambda x: x not in a, b))

    return intersection, reunion, a_minus_b, b_minus_a


print("2. " + str(list_ops([1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8, 8])))

'''
Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x. 
Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite. 
Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 
se va returna [1, 2, 3, 4] # 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.
'''


def counter(lists, app):
    merged = list(itertools.chain(*lists))
    different_items = set(merged)

    apparitions = list(map(lambda x: merged.count(x), different_items))
    return list(filter(lambda x: x[1] == app, zip(different_items, apparitions)))


print("3." + str(counter([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2)))
