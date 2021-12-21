"""
Faça um algoritmo que leia um número positivo e imprima seus divisores
"""

num = int(input("Digite um número inteiro positivo: "))
lista = []

if num < 0:
    num = int(input("Número digitado não pode ser menor que 0. Digite um número inteiro positivo"))
for count in range(1, num + 1):
    if num % count == 0:
        lista.append(count)

print(f"Os divisores de {num} são {lista}")