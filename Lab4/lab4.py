'''
1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
a) a-b
b) a+b
c) a/b
d) a*b
'''
import os


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


def printInfo(path):
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
printInfo("E:\\Downloadsad")
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
