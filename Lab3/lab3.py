'''1. Sa se scrie o functie care primeste ca parametri doua liste a si b
    si returneaza un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a)
'''


def ex1(a, b):
    intersection = map(lambda x: x in b, a)
    reunion = set(a + b)
    a_minus_b = map(lambda x: x not in b, a)
    b_minus_a = map(lambda x: x not in a, b)

    return intersection, reunion, a_minus_b, b_minus_a


'''2. Scrieti o functie care primeste ca parametru un sir de caractere si 
returneaza un dictionar in care cheile sunt caracterele dn componenta sirului de caractere 
iar valorile sunt reprezentate de numarul de aparitii ale caracterului respectiv in textul dat.
Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul:
 {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.'''


def ex2(i):
    def go(l, d):
        if len(l) == 0:
            return d

        if l[0] in d.keys():
            d[l[0]] = d[l[0]] + 1
        else:
            d[l[0]] = 1

        return go(l[1:], d)

    return go(i, {})


print(ex2("Ana are mere"))
