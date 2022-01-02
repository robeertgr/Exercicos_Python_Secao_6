"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""

count = 1
soma = 0

while count <= 100:
    if count % 2 == 0:
        soma = soma + count
    count = count + 1

print(soma)
