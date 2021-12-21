"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela,
como resultado, a correspondente média aritmética. O número de notas com que o aluno
pretanda efetuar o cálculo não será fornecido pelo programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.
"""

soma, media, count = 0, 0, 0
nota = float(input("Digite uma nota: "))

while nota >= 10 and nota <= 20:
    soma += nota
    count += 1
    if nota >= 10 and nota <= 20:
        nota = float(input("Digite uma nota: "))
        
media = soma / count
print(f"Média aritmética: {media}")
