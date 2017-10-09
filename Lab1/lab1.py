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


def vowel_count(word):
    return len(list(filter(lambda x: x in "aeiouAEIOU", word)))


print("2. " + str(vowel_count("This is a sentence with 9 vowels.")))

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


def is_upper(c):
    if c.isupper():
        return "_" + c.lower()
    else:
        return c


def convert(string):
    return "".join(map(lambda x: is_upper(x), string))


print(convert("UpperCamelCase"))

'''
Se da un sir de caractere care reprezinta un polinom (Ex: "3x^3 + 5x^2 - 2x - 5") 
si un numar (intreg sau float). Sa se evalueze polinomul respectiv pentru valoarea data.
'''


def compute(polynomial, value):
    # replacing x with value
    fixed = polynomial.replace("x", "*" + str(value))

    print(fixed)
    # list of operands and numbers
    agents = re.findall("[0-9]+|-|\*|\^|\+", fixed)

    nums = agents[0::2]
    ops = agents[1::2]

    for i in range(0, len(agents[1::2])):
        print(nums[i] + " " + ops[i] + " " + nums[i + 1])

compute("21x^2 + 13x^2 + 3x - 3", 4)

'''
Scrieti o functie care sa returneze cel mai mare numar prim dintr-un sir de caractere dat ca parametru 
    sau -1 daca sirul de caractere nu contine nici un numar prim. 
Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
'''


def replace_alpha(c, y):
    # if current letter is followed by a digit, return a space to distinguish between numbers
    if c.isalpha() and y.isdigit():
        return " "
    # if its digit, return it as it is
    elif c.isdigit():
        return c
    # if its only a letter follow by some other letter, erase it
    elif c.isalpha():
        return ""


def is_prime(input):
    return all(map(lambda x: input % x != 0, list(range(2, input / 2))))


def biggest_prime(input):
    # parsing the list 2 consecutive letters at a time; added " " so it fully parses it
    removed_letters = map(lambda z, y: replace_alpha(z, y), list(input), list(input[1:] + " "))

    # filtering out the "" elements, and created a string that would look like: " 27 75 271 1"
    removed_empty_indexes = "".join(filter(lambda y: not y == "", removed_letters))

    # using regexes to filter out the numbers, then removing the empty "" and transforming them into actual ints
    list_of_numbers = map(lambda x: int(x), filter(lambda x: x != "", re.findall("[0-9]*", removed_empty_indexes)))

    # filtering only the primes
    result = filter(lambda x: is_prime(x), list_of_numbers)

    # returning the appropiate result
    if len(result) == 0:
        return -1
    else:
        return max(result)


a = biggest_prime("ahsfaisd35biaishai23isisvdshcbsicidsbfsd97sidsda271")
print(a)
