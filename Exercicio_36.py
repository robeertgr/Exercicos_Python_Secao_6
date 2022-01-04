"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros
10 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez
primeiros números naturais é:
    1² = 2² + ... 10² = 385
O quadrado da soma dos dez primeiros números naturais é:
    (1 + 2 + ... + 10) ² = 
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o
quadrado da soma é 3025 - 385 = 2640
"""

quadr = soma = soma_quadr = subtr = 0


for count in range(1, 11):
    quadr = count * count
    soma += quadr
    soma_quadr += count

soma_quadr *= soma_quadr
subtr = soma_quadr - soma

print(soma)
print(soma_quadr)
print(subtr)