"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos e imprima sua média
"""

soma = 0

for num in range(1, 11):
    num = int(input("Digite um número: "))
    if num > 0:
        soma = soma + num
media = soma / 10
print(f"A média é {media}")
  