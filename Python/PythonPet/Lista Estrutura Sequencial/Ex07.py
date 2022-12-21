# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
# Uma lista com todos os números

numeros = []
i = 0

while len(numeros) != 5:
   i += 1
   print("Diga o número " + str(i) + "º:")
   try:
       numero = int(input())
   except:
       print("Número inválido.")
       i -= 1
       continue
   numeros.append(numero)

print("Números: " + ", ".join(str(numero) for numero in numeros))
soma = sum(numeros)
print("Soma: " + str(soma))
multiplicacao = 1
for numero in numeros:
   multiplicacao = multiplicacao * numero
print("Multiplicação: " + str(multiplicacao))
