"""
Faça um programa que peça ao usuário para digitar 10 valores
e some-os.
"""

soma = 0
for n in range(1, 11):
    num = int(input("Informe um número: "))
    soma = soma + num
print(f"Resultado da soma: {soma}")