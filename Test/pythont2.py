import json
import re
import zipfile

'''
Sa se implementeze functia problema1(n). Functia primeste un parametru n - numarul natural mai mare ca 0.
Functia va returna o lista cu primele n numere naturale mai mari strict ( > ) decat 30.
Spre exemplu problema1(3) va returna [31, 32, 33].
'''


def problema1(n):
    if n <= 0:
        return []
    else:
        return list(range(30, 30 + n + 1))[1:]  # dropping head which is 30


'''
Sa se implementeze functia problema2(big_string, small_string). 
Functia primeste ca parametri doua stringuri: big_string si small_string.
 Functia va returna True daca small_string apare in big_string de doua (2) ori. 
 Spre exemplu problema2(big_string="123456", small_string="12") va returna False 
 si problema2(big_string="123412",small_string="12") va returna True.
'''


def problema2(big_string, small_string):
    return len(re.findall(small_string, big_string)) >= 2


'''
Sa se implementeze functia problema3(x).
 Functia primeste ca parametru un numar natural x mai mare (strict) ca 1. 
 Functia va returna rezultatul polinomului 2 * pow(x, 3) - pow(x, 2) - x + 3.
  Unde pow(x, 2) reprezinta x la puterea 2. Spre exemplu problema3(x=2) va returna 13.
'''


def problema3(x):
    return 2 * (x ** 3) - x ** 2 - x + 3


'''
Sa se implementeze functia problema4(apath). 
Functia primeste parametru apath - calea catre o arhiva. 
Functia va intoarce o lista cu numele fisierelor din arhiva ce contine string-ul "file" in nume. 
Spre exemplu problema4(apath="arhiva.zip") 
    - unde arhiva.zip contine ["file1.txt", 
    "file2.exe", "file3.dll", "different_file.txt", "different_file.exe"] 
    - va returna lista ["file1.txt", "file2.exe", "file3.dll", "different_file.txt", "different_file.exe"] . 
Observatie: arhivele primite ca parametru vor avea tot timpul doar fisiere in root - fara foldere si subfoldere.
'''


def problema4(apath):
    try:
        file = zipfile.ZipFile(apath)
        return file.namelist()
    except Exception as e:
        raise e


'''
Sa se implementeze functia problema5(astr). 
Functia primeste ca parametru un string astr ce reprezinta serializarea in json a unei liste. 
Functia va returna lungimea listei serializate. Spre exemplu un apel problema5(astr='[1, 2, 3, 4, 5]') intoarce 5.
'''


def problema5(astr):
    return len(json.load(astr))

'''
Sa se implementeze functia problema6(alink). 
Functia primeste ca parametru un url alink.
 Functia va returna True daca in continutul obtinut de pe acel link se gaseste substringul "TESTPYTHON". 
 Spre exemplu problema6(alink="http://md5.jsontest.com/?text=example_text") va returna False.
'''


def problema6(alink):
    import urllib.request
    try:
        link_content = urllib.request.urlopen(alink).read()
        r = re.compile("TESTPYTHON")
        content = re.search("TESTPYTHON", link_content)

        if r.finditer(content):
            return True
        else:
            return False
    except Exception as e:
        raise e
