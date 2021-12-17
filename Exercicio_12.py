"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de N até 0 em ordem decrescente.
"""

num = int(input("Digite um número: "))

for count in range(num, 0, -1):
    print(count)
