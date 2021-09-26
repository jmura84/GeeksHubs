import unittest
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def doblar(a):
    return a * 2

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def cuadrado(a):
    return pow(a, 2)

def raiz(a):
    return math.sqrt(a)

def es_par(a):
    return 1 if a % 2 == 0 else 0


if __name__ == '__main__':
    print(sumar(2, 3))
    print(restar(9, 2))
    print(doblar(999))
    print(multiplicar(53, 2))
    print(dividir(23, 131))
    print(cuadrado(22))
    print(raiz(4))
    print(es_par(22))