"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os 
números ímpares de N até 1 em ordem decrescente.
"""

num = int(input("Digite um número impar: "))
while num % 2 == 0:
    num = int(input("Número não é impar. Digite um número ímpar: "))
if num % 2 != 0:
    for count in range(num, -1, -2):
        print(count)
