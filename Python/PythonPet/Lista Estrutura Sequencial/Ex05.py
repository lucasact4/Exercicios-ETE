# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
print('Informe os numeros:')
for i in range(20):
	listaNumeros.append((int(input('Numero: ' + str(i+1) + ':\n'))))
	numero = listaNumeros[i]
	if(numero%2 == 0):
		listaPar.append(numero)
	else:
		listaImpar.append(numero)

print(listaNumeros)
print(listaPar)
print(listaImpar)
