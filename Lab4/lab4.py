'''
1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
a) a-b
b) a+b
c) a/b
d) a*b
'''


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


ops(3, 0)