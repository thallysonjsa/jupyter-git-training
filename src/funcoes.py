import math

def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

def quadrado(x):
    return math.pow(x)

def tem_par(lista):
    for numero in lista:
        if numero % 2 == 0:
            return True
    return False