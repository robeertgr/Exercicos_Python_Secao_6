"""
Faça um programa que receba dois números. Calcule e mostre:
- a soma dos números pares desse intervalo de números, incluindo os números digitados;
- a multiplicação dos números ímpares desse intervalo, incluindo os digitados.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma_par, soma_impar = 0, 1

if num1 > num2:
    for x in range(num2, num1 + 1):
        if x % 2 == 0:
            soma_par += x
        else:
            soma_impar *= x
    print(f"No intervalo entre {num2} e {num1} a soma deles é {soma_par}")
    print(f"No intervalo entre {num2} e {num1} a multiplicação deles é {soma_impar}")
else:
    for x in range(num1, num2 + 1):
        if x % 2 == 0:
            soma_par += x
        else:
            soma_impar *= x
    print(f"No intervalo entre {num1} e {num2} a soma deles é {soma_par}")
    print(f"No intervalo entre {num1} e {num2} a multiplicação deles é {soma_impar}")
