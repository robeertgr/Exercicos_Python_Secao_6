"""
Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como
saída o número de cada dado e a relação entre eles (>, < ou =) de cada lançamento.
"""

import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

if d1 > d2:
    print("Dado 1 é maior que dado 2\n"
         f"Dado 1 = {d1}\n"
         f"Dado 2 = {d2}")
elif d2 > d1:
    print("Dado 2 é maior que dado 1\n"
         f"Dado 1 = {d1}\n"
         f"Dado 2 = {d2}")
elif d2 == d1 and d1 == d2:
    print(f"Os dados são iguais!\n"
          f"Dado 1 = {d1}\n"
          f"Dado 2 = {d2}")