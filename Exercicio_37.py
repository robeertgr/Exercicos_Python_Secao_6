"""
Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive)
possuem a seguinte propriedade: a soma dos dois dígitos de mais baixa ordem com os dois
digitos de mais alta ordem elevada ao quadrado é igual ao próprio número. Por exemplo,
para o inteiro 3025, temos que:
    30 + 25 = 55
    55² = 3025
"""

soma = 0

for i in range(1000, 10000):
    soma = ((i // 100) + (i % 100))
    if ((soma * soma) == i):
        print(f"Os números entre 1000 e 9999 que possui a mesma propriedade são: {i}")