# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
listaNumeros = []
print ('Informe os 5 numeros')
for i in range(5):
	listaNumeros.append(input('Numero '+ str(i+1) + ':\n'))
print(listaNumeros)
