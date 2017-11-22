'''
1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
a) a-b
b) a+b
c) a/b
d) a*b
'''
import getpass
import os

import sys
import platform
import multiprocessing


def ops(a, b):
    try:
        print(a - b)
        print(a + b)
        print(a / b)
        print(a * b)
    except TypeError:
        print("Provide numbers please")
    except ArithmeticError as e:
        print("Error computing!")


print("1. ")
ops(3, 0)
print("\n\n")

'''
2. Scrieti un script care primeste ca parametru de la linia de comanda un path si
afiseaza primii 4096 bytes daca path-ul duce la un fisier, 
intrarile din acesta daca path-ul reprezinta un director 
si un mesaj de eroare daca path-ul nu este unul valid.'''


def print_Info(path):
    try:
        if not os.path.exists(path):
            raise IOError("Invalid path")

        if os.path.isdir(path):
            print("dir")
            print(os.listdir(path))
        elif os.path.isfile(path):
            with open(path) as file:
                print(file.read(4096))
    except IOError as e:
        print(e)
        print("Provide a valid file/dir!")
    except Exception as e:
        print(e)


print("2. ")
print_Info("E:\\Downloadsad")
print("\n\n")

'''
3. Scrieti o functie care primeste ca parametru un nume de fisier. 
Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar, 
sub forma cheie [tab] valoare.
'''


def environ(path):
    try:
        if not os.path.isfile(path):
            raise IOError("Proper file please")

        with open(path, "w") as f:
            zipped = zip(os.environ.keys(), os.environ.values())
            output = list(map(lambda x: str(x[0]) + "   " + str(x[1]), zipped))
            for line in output:
                f.write(line + "\n")
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


print("3. ")
environ("E:\\test.txt")
print("\n\n")

'''
9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem: 
versiunea de python folosita.
Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ===" 
iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
numele user-ului care a executat scriptul, 
path-ul complet al scriptului.
path-ul directorului in care se afla scriptul, 
tipul sistemului de operare, 
numarul de core-uri, 
directoarele din PATH-ul procesului cate unul pe linie, 
'''


def system_information():
    python_version = sys.version_info
    if python_version[0] == 3:
        print("Running under Py3")
    elif python_version[0] == 2:
        print("=== Python 2 ===")
    else:
        print("Python")

    print("User " + getpass.getuser())

    script_path = os.path.realpath(__file__)
    directory = "\\".join(script_path.split("\\")[0:-1])

    print(script_path)
    print(directory)
    print(platform.system() + " " + platform.release())
    print(platform.processor())
    print(multiprocessing.cpu_count())


print("9. ")
system_information()
