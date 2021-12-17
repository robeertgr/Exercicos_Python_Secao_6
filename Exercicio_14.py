"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de N até 0 em ordem decrescente.
"""

num = int(input("Digite um número par: "))
while num % 2 != 0:
    num = int(input("Número não é par. Digite um número par: "))
if num % 2 == 0:
    for count in range(num, -2, -2):
        print(count)