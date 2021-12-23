"""
Escreva um programa para calcular o valor da série, para 5 termos.
    S = 0 + 1/2! + 2/4! + 3/6! + ...
"""

import math

s = 0
for n in range(2, 6, 2):
    s = 1 / math.factorial(n)
    print(s)
