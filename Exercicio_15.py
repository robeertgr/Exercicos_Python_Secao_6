"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números
ímpares de 1 até N em ordem crescente.
"""

num = int(input("Digite um número impar: "))
while num % 2 == 0:
    num = int(input("Número não é impar. Digite um número impar: "))
if num % 2 != 0:
    for count in range(1, num + 2, 2):
        print(count)
