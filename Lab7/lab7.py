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
timer(1, 2)
