import timeit
from os import listdir
from os.path import isfile, join
'''
1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie (din intervalul [a, b] ,
unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul (in minute, cu doua zecimale).
Programul va rula la infinit.
'''


def timer(a, b):
    import time
    start = time.time()

    while 1:
        from random import randint
        x = randint(a, b)
        time.sleep(x)

        current = time.time()

        mins = (current - start) // 60 + round((current - start) % 60 / 100, 2)
        print(mins)


print("Ex 1.")
#timer(1, 2)
print("\n\n\n")

'''
2. Scrieti doua functii de verificare daca un numar este prim, 
si verificati care dintre ele este mai eficienta din punct de vedere al timpului.
'''


def is_prime1(x):
    def go():
        for i in range(2, int(x / 2)):
            if x % i == 0:
                return False

        print("prime\n")
        return True

    print(timeit.timeit(go))


def is_prime2(x):
    def go():
        if x <= 3:
            return True

        if x % 2 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6

        print("prime\n")
        return True

    print(timeit.timeit(go))


print("ex 2.")
is_prime1(12345678912312312331231241235)
is_prime2(12345678912312312331231241235)


'''
3. Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare. 
Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt. 
'''


def duplicates(directory, output_dir):
    def g():
        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        print(files)
        output = ""
        set_files = set(files)

        for file in set_files:
            if files.count(file) > 2:
                output += file

        print(output)

    print(timeit.timeit(g()))

print("ex3.\n")
duplicates("E:\\books", "E:\\output.txt")

'''
4. Sa se scrie un script care primeste ca argument un director
 si creeaza un fisier JSON cu date despre toate fisierele din acel director. 
 Pentru fiecare fisier vor fi afisate urmatoarele informatii: 
    nume_fisier, 
    md5_fisier, 
    sha256_fisier, 
    size_fisier (in bytes), 
    cand a fost creat fisierul (in format human-readable) 
    si calea absoluta catre fisier.
'''



'''
5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate. 
Primul script va salva periodic o lista cu toate fisierele dintr-un director 
iar al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb
 si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).
'''



'''
6. Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou, 
pentru ultimii x ani (x este dat ca argument).
'''


'''
7. Sa se simuleze extragerea 6/49. 
'''