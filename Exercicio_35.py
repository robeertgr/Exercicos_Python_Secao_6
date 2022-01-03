"""
Faça um programa que some os números impares contidos em um intervalo definido
pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo
e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o
usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve
ser esrito uma mensagem de erro na tela, "Intervalo de valores inválidos" e o programa
termina. Exeplo de tela de saída: 
Digite o valor inicial e o valor final: 5 10
Soma dos ímpares neste intervalo: 21
"""
soma = 0

inicial = int(input("Digite um valor inicial: "))
final = int(input("Digite um valor final: "))

while inicial > final:
    print("Intervalo de valores inválidos\n"
          "Fim de programa!")
    break

for count in range(inicial, final):
    if count % 2 != 0:
        soma += count

print(f"Soma dos ímpares neste intervalo: {soma}")