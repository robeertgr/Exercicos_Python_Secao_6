"""
Faça um programa que leia um número inteiro positivo N e calcule a soma
dos N primeiros números naturais
"""

num = int(input("Informe um número inteiro positivo: "))
soma = 0
while num < 0:
    num = int(input("Número não é positivo. Informe um número inteiro positivo: "))
if num >= 0:
    for num in range(1, num):
        soma = soma + num
        print(soma)
