"""
Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos
de 3 ou 5.
"""

soma = 0

for count in range(1, 1000):
    if count % 3 == 0 or count % 5 == 0:
        soma += count

print("A soma de todos os números naturais abaixo de 1000 que são\n"
     f"multiplos de 3 ou 5 é {soma}")