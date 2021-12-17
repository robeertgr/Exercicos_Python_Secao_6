"""
Faça um programa que leia um número inteiro N e depois imprima os
N primeiros números naturais ímpares
"""

num = int(input("Digite um número: "))
count, aux = 1, 1
while count <= num:
    if aux % 2 != 0:
        print(aux)
        count = count + 1
    aux = aux + 1
