"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem crescente.
"""

num = int(input("Digite um número: "))

for count in range(1, num + 1):
    print(count)
