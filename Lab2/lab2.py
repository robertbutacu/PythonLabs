import re


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
