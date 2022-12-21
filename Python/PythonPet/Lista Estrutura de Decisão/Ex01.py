# 1. Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
  print(f'O primeiro número: {n1} é MAIOR que o segundo número: {n2}!')
elif n2 > n1:
  print(f'O segundo número: {n2} é MAIOR que o primeiro número: {n1}!')
else:
  print(f"Os dois números que são {n1} e {n2} são IGUAIS!")
  