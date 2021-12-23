"""
Faça um programa para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... + (2n - 1)
"""

soma1 = 0
soma2 = 0
soma3 = 0
numero = int(input("Digite um número inteiro: "))
 
for i in range(1, 2 * numero):
    if i <= numero:
        soma1 += i
    if i % 2 == 0:
        soma2 -= i
    else:
        soma2 += i
        soma3 += i
 
print(f'{soma1}\n{soma2}\n{soma3}')