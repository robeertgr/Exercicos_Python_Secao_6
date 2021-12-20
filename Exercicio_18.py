"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
fornecido pelo usuário.
"""

rep = int(input("Informe quantos números devem ser lidos: "))
maior = 0

for count in range(1, rep + 1):
    num = int(input("Informe um número: "))
    if num > maior:
        maior = num
        vezes = 1
    elif num == maior:
        vezes += vezes

print(f"O maior número recebido foi {maior}"
      f"\nEle foi repetido {vezes} vezes")
