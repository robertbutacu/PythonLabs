import re

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

'''
5. Fie functia validate_dict care primeste ca parametru un set de tuple
 care reprezinta reguli de validare pentru un dictionar 
 cu chei de tipul string si valori tot de tipul string si un dictionare. 
 O regula este definita astfel: (cheie, "prefix", "middle", "sufix"). 
 O valoare este considerata valida daca incepe cu "prefix", "middle" se gaseste in interiorul valorii
  (nu la inceput sau sfarsit) si se sfarsete cu "sufix". 
  Functia va returna True daca dictionarul dat ca parametru respecta toate regulile, False in caz contrar. 
Exemplu: regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] 
si dictionarul 
{"key2": "starting the engine in the middle of the winter", 
"key1": "come inside, it's too cold outside", "key3": "this is not valid"} 
=> False deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3" care nu apare in reguli.'''


def validate_dict(rules, dictionary):
    def create_regex(*k):
        print(r'{0}'.format(".".join(k)))
        return r'{0}'.format(" * ".join(k))

    def is_regex_valid(regex, string):
        print(regex + " " + string + "\n")
        compiled = re.compile(regex)
        return re.search(compiled, string) is not None

    def is_valid(rules, pair):
        valid = False

        for rule in rules:
            # print(str(pair) + " " + str(rule) + "\n")
            if rule[0] == pair[0]:
                if is_regex_valid(create_regex(rule[1], rule[2], rule[3]), pair[1]):
                    valid = True

        return valid

    for a in dictionary:
        if not is_valid(rules, (a, dictionary[a])):
            return False

    return True


print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                    {"key2": "starting the engine in the middle of the winter",
                     "key1": "come inside, it's too cold outside", "key3": "this is not valid"}
                    ))

'''
6. Fie un dictionar global
{    
    "+": lambda a, b: a + b,     
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}
 Sa se construiasca o functie apply_operator(operator, a, b) 
 'care va aplica peste a si b regula specificata de dictionarul global.
  Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara modificarea functiei. 
'''

'''
8. Sa se scrie o functie care primeste ca parametru o lista 
si returneaza un tuplu (a, b), a reprezentand numarul de elemente unice din set iar b reprezentand numarul de elemente duplicate din set.
'''


def ex8(inputt):
    count = list(map(lambda x: inputt.count(x), inputt))
    zipper = set(zip(inputt, count))

    unique = list(filter(lambda x: x[1] == 1, zipper))
    duplicates = list(filter(lambda x: x[1] == 2, zipper))

    return unique, duplicates


print(ex8([1, 2, 3, 1, 2, 3, 1, 33]))

'''
9. Sa se scrie o functie care primeste un numar variabil de seturi 
si returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua: 
reuniune, intersectie, a-b, b-a.
 Cheia va avea urmatoarea forma: "a op b", unde a si b sunt doua seturi, iar op este operatorul aplicat: |, &, -. 
{
    "{1, 2} | {2, 3}": 3,
    "{1, 2} & {2, 3}": 1,
    "{1, 2} - {2, 3}": 1,
    ...
}
'''


def ex9(*args):
    result = dict()

    for a in args:
        for b in args:
            if not a == b:
                result[str(a) + " | " + str(b)] = a + b
                result[str(a) + " & " + str(b)] = set(a + b)
                result[str(a) + " - " + str(b)] = set(a) ^ set(b)
                result[str(b) + " - " + str(a)] = set(b) ^ set(a)

    return result


dictionary = ex9((1, 23), (1, 1, 1), (2312, 1231, 123))
for a in dictionary:
    print(str(a) + " : " + str(dictionary[a]) + " \n")
