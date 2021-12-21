"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""

num = int(input("Digite um número: "))

while True:
    num += 1
    if num % 11 == 0:
        print(f"O número {num} é múltiplo de 11.")
        break
    elif num % 13 == 0:
        print(f"O número {num} é multiplo de 13.")
        break
    elif num % 17 == 0:
        print(f"O número {num} é multiplo de 17.")
        break
    