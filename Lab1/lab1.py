import re

'''
Cel mai mare divizor comun a mai multor numere (definiti o functie cu numar variabil de parametri care sa rezolve acest lucru)
'''


def gcd(x, y):
    if x == y:
        return x
    else:
        return gcd(max(x, y) - min(x, y), min(x, y))


print("1. " + str(gcd(8, 4)))


'''
Scrieti o functie care calculeaza cate vocale sunt intr-un sir de caractere
'''


def vowelcount(word):
    return len(list(filter(lambda x: x in "aeiouAEIOU", word)))


print("2. " + str(vowelcount("This is a sentence with 9 vowels.")))

'''
Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )
'''


def wordcount(sentence):
    return len(re.findall("[a-zA-Z]+", sentence))

print("3. " + str(wordcount("This, . is  ... a  ,,,sentence .,")))


'''
Scrieti o functie care primeste ca parametri doua siruri de caractere 
si care returneaza numarul de aparitii ale primului sir de caractere in al doilea.
'''


def apparitions(s1, s2):
    count = 0
    for i in range(0, len(s2)):
        if s2[i:(i + len(s1))] == s1:
            count += 1
    return count


print("4. " + str(apparitions("a", "aaab")))


'''
Scrieti o functie care converteste in sir de caractere scris UpperCamelCase in lowercase_with_underscores.
'''


def isUpper(c):
    if c.isupper():
        return "_" + c.lower()
    else:
        return c


def convert(string):
    return "".join(map(lambda x: isUpper(x), string))


print(convert("UpperCamelCase"))


'''
Se da un sir de caractere care reprezinta un polinom (Ex: "3x^3 + 5x^2 - 2x - 5") 
si un numar (intreg sau float). Sa se evalueze polinomul respectiv pentru valoarea data.
'''


def compute(polynomial, value):
    fixed = re.sub("[1-9]+x", )