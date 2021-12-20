"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá
ser informado o número de dados lidos e número de valores pares. O processo terminará
quando for digitado o número 1000.
"""
num_lidos = 0
num_par = 0
num = int(input("Digite um número: "))
while (num != 1000):
    if num % 2 == 0:
        print(f"Número {num} é par.")
        num_par = num_par + 1
    else:
        print(f"Número {num} não é par")
    num_lidos = num_lidos + 1
    num = int(input("Digite um número: "))

print(f"Números lidos: {num_lidos}"
      f"\nNúmeros pares: {num_par}")
print("Fim de programa.")