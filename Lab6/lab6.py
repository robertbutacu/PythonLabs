'''
Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru.
Un cuvant este definit ca o secventa de caractere alfa-numerice.
'''
import re


def extract(text):
    result = re.findall("\w+", text)

    print(result)


print("Ex1. ")
extract("asdf asdfasdf :? -= ar 3 1231 a sdf43 asdf ar 23edw")

'''
Sa se scrie o functie care primeste ca parametru un sir de caractere regex, 
un sir de caractere text si un numar intreg x 
si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.
'''


def match(regex, text, x):
    result = re.findall(regex, text)

    return list(filter(lambda f: len(f) <= x, result))


print("Ex 2.")
print(match("\w+", "asdf asdfasdf :? -= ar 3 1231 a sdf43 asdf ar 23edw", 2))

'''
Sa se scrie o functie care primeste ca parametru 
un sir de caractere text 
si o lista de expresii regulate 
si returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.
'''


def matchers(text, list_of_regex):
    from setuptools.namespaces import flatten
    return set(flatten(map(lambda regex: re.findall(regex, text), list_of_regex)))


print(matchers("asdf aer23 asdf2q asdf 23 asdf 2     asdf", ["\w+", "[a-z]", "\s", "\d"]))

'''
Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale. 
Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * .
'''


def transform(text):
    def transform_character(word):
        def go(pair):
            if pair[1] % 2 == 1:
                return "*"
            else:
                return pair[0]

        zipped = list(zip(list(word.group(0)), range(0, len(list(word.group(0))))))

        return "".join(list(map(lambda x: go(x), zipped)))

    vowels = "(a|e|i|o|u|A|E|I|O|U)"

    print(re.sub("({0}\w+{1})".format(vowels, vowels), transform_character, text))


print("Ex 5.")
transform("asdfaasdfe asdfarbiunwu afgdsbdfb dgs fg")

'''
Sa se scrie o functie care parcurge recursiv un director 
si afiseaza acele fisiere a caror nume face match pe o expresie regulata data ca parametru 
sau contine un sir de caractere care face match pe aceeasi expresie. 
Fisierele care satisfac ambele conditii vor fi afisate prefixate cu ">>" 
'''


def recursive_match(dir, regex):
    def contents_match(file, regex):
        try:
            with open(file, "r") as f:
                return re.match(regex, f.read())
        except UnicodeDecodeError as e:
            raise e

    try:
        import os
        if not os.path.isdir(dir):
            raise NotADirectoryError("Provide a valid directory!")

        for root, dirs, files in os.walk(dir):
            for file in files:
                matches_file_name = re.match(regex, file)
                matches_file_contents = contents_match(root + "\\" + file, regex)

                if matches_file_contents and matches_file_contents:
                    print(">>{0}".format(file))
                elif matches_file_contents or matches_file_name:
                    print(file)

    except NotADirectoryError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)


print("Ex 7.")
recursive_match("E:\\information-security", "\w+")
