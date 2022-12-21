# 7. Faça um programa que leia 5 números e informe o maior número.
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))
if (num1 >num2 and num1 > num3 and num1 > num4 and num1  >num5):
	print("o maior numero é o 1º:", num1)
if (num2 >num1 and num2 > num3 and num2 > num4 and num2  >num5):
	print("o maior numero é o 2º:", num2)
if (num3 >num2 and num3 > num1 and num3 > num4 and num3  >num5):
	print("o maior numero é o 3º:", num3)	
elif (num4 >num2 and num4 > num3 and num4 > num1 and num4  >num5):
	print("o maior numero é o 4º:", num4)	
else:
	print("o maior numero é o 5º:", num5)
    