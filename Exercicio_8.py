"""
Escreva um programa que leia 10 números inteiros e escreva o menor
e maior valor lido.
"""

maior = 0
menor = 0

for num in range(1, 11):
    num = int(input(f"Digite um número {num}/10: "))
    if num > maior:
        maior = num
    else:
        menor = num
        
print(f"Maior = {maior}\n"
      f"Menor = {menor}")
