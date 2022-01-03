"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1
a 20. Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""
 
from math import gcd

def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

numeros = range(2, 21)
print(mmc(numeros)) # 232792560