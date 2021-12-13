"""
2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while e a terceira do while.
"""

for x in range(1, 101):
    print(x, end=' ')

y = 1
print("\n")
while y <= 100:
    print(y, end=' ')
    y = y + 1

z = 1
print("\n")
while True:
    print(z, end=' ')
    z = z + 1
    if z > 100:
        break
