"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir
    E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""

import math

resultado = 1
n = int(input("Digite um número: "))

for n in range(2, n + 1):
    fatorial = math.factorial(n)
    resultado += 1 / fatorial

print(f"Resultado da fórmula: {resultado}")
