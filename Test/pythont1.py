import sys
from os import listdir, os
from os.path import isdir, getsize
from os.path import isfile
from os.path import join

'''
Sa se scrie o functie cu numele problema2 ce va returna suma primelor 5 numere naturale pare mai mari decat zero.

'''


def problema2():
    def go(current, sum, index):
        if index > 5:
            return sum

        return go(current + 2, sum + current, index + 1)

    return go(2, 0, 1)


'''
Sa se scrie o functie cu numele problema3 ce primeste ca parametru un numar natural n. 
Aceasta va returna numarul de divizori ai lui n. Exemplu: n=3, return: 2; n = 4, return: 3
'''


def problema3(n):
    try:
        if n <= 0:
            raise ValueError("n must be greater than 0!")

        return len(list(filter(lambda x: n % x == 0, range(1, int(n) + 1))))

    except ValueError as e:
        return e


'''
Sa se scrie o functie cu numele problema4 ce primeste ca parametru un numar natural m. 
Aceasta va returna o lista cu primele m numere naturale ce au minim 3 divizori.
 Pentru a rezolva aceasta problema, apelati functia definita la Problema 3.
'''


def problema4(m):
    try:
        if m <= 0:
            raise ValueError("m must be greater than 0!")

        curr = 1
        result = []
        while m > 0:
            if problema3(curr) >= 3:
                m = m - 1
                result = result + [curr]
                curr = curr + 1
            else:
                curr = curr + 1
        return result
    except ValueError as e:
        return e


'''
Sa se scrie o functie cu numele problema5 ce primeste ca parametru o lista my_list. 
Functia va returna un dictionar de forma {e1: count_e1, e2: count_e2, etc} 
in care e1, e2,.. en sunt elemente din lista initiala, iar count_ei reprezinta numarul de aparitii al lui ei in lista my_list.
'''


def problema5(my_list):
    set_of_my_list = set(my_list)

    result = {}
    for elem in set_of_my_list:
        result[elem] = my_list.count(elem)

    return result


'''
Sa se scrie o functie cu numele problema6 ce primeste doua cai ca parametri: folder si fisier.
 Implementati functia 
 astfel incat in fisierul de la calea fisier sa fie scrisa pe cate o linie calea absoluta a fiecarui fisier,
  din interiorul directorului de la calea folder, ce are size-ul mai mare de 10 bytes.
'''


def problema6(folder, file):
    try:
        f = open(file, "w")
        only_files = [[f for f in listdir(folder) if isfile(join(folder, f))]]

        for file_found in only_files:
            stats = os.path.getsize(file_found)

            if stats.st_size > 10:
                f.write(file)
    except Exception as e:
        print(e)


'''
Sa se scrie o functie cu numele problema7 ce primeste doi parametri: director, depth. 
Functia va returna o lista cu toate caile abosolute pentru subfolderele din director cu adancimea depth
 ce nu au in interior niciun fisier cu size-ul mai mare de 1024 bytes. 
 Subdirectoarele din folderul de input director au adancime 1.
'''


def problema7(directory, depth):
    def go(curr_dir, curr_depth):
        try:
            files = [[f for f in listdir(curr_dir) if isfile(join(curr_dir, f))]]
            dirs = [[f for f in listdir(curr_dir) if isdir(join(curr_dir, f))]]

            result = []
            if all(lambda x: os.path.getsize(x) > 1024, files):
                result += os.path.abspath(curr_dir)

            if curr_depth == depth:
                return result
            else:
                for dirr in dirs:
                    result += go(dirr, curr_depth + 1)
                return result
        except Exception as e:
            return e

    return go(directory, 0)


print(problema7("E:\\books", 2))

if __name__ == "__main__":
    if "-silent" not in sys.argv:
        print("Noise")
