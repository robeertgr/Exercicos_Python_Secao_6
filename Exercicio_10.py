"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""

count = 1
while count <= 50:
    if count % 2 == 0:
        print(count)
    count = count + 1
