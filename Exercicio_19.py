"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número.
"""
num = int(input("Digite um número entre 100 e 999: "))

while num < 100 or num > 999:
    num = int(input("Número digitado não está entre 100 e 999. Digite um número entre 100 e 999: "))
for digito in enumerate(num.__str__()):
    print(digito)
 