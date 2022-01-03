"""
Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo:
Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
"""

mult_i = mult_j = 0

n = int(input("Digite um número: "))
i = int(input("Digite um número: "))
j = int(input("Digite um número: "))

while n <= 0 or i <= 0 or j <= 0:
    print("Nenhum dos 3 números podem ser menores ou iguais a 0!")
    n = int(input("Digite um número: "))
    i = int(input("Digite um número: "))
    j = int(input("Digite um número: "))

for count in range(n):
    if mult_i == mult_j:
        print(mult_i)
        mult_i += i
        mult_j += j
    elif mult_i < mult_j:
        print(mult_i)
        mult_i += i
    else:
        print(mult_j)
        mult_j += j
