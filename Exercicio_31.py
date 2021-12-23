"""
Faça um programa que calcule e escreva o valor de S
    S = 1/1 + 3/2 + 5/3 + 7/4 + ... 99/50
"""

dem = 0
soma = 0

for n in range(1, 99+1, 2):
    dem += 1
    div = n / dem
    soma += div
print(soma)