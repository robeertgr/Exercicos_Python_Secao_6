"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é 
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

soma = 0
num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    num = int(input("Número não pode ser negativo. Digite um número inteiro positivo: "))

for count in range(1, num):
    if num % count == 0:
        soma += count
        
print(f"A soma de todos os divisores de {num} é {soma}")