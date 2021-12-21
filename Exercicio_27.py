"""
Em matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e acrescente o valor de H(n)
"""

harmonico = 0
n = int(input('Digite um numero: '))

for count in range(1, n + 1): 
    harmonico += (1 / count)

print(f'O número harmônico é: {harmonico}')
