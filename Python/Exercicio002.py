#Ex 1 = Descrição Narrativa
#Passo 1 - Obter os dois números que serão multiplicados. EX: 10 + 15
#Passo 2 - Multiplicar os números. EX: somar
#Passo 3 - Mostrar o resultado obtido na multiplicação. EX: resposta = 150
#Ex 2 = Fluxograma
#Início > Recebimento de dados > Multiplicação/uso dos dados > Resultado e apresentação da multiplicação > Fim
#Ex 3 = Pseudocódigo
#Início
nome = input('Para começar, digite seu nome: ')
print('Eae {}? vamos multiplicar ?'.format(nome))
#Passo 1 + Recebimento de dados
num1 = int(input('Digite um valor aqui: '))
num2 = int(input('Digite outro valor aqui: '))
#Passo 2 + Multiplicação/uso dos dados
mult = num1 * num2
#Passo 3 + Resultado e apresentação da multiplicação
print('A multiplicação entre {} e {} é igual a {}!'.format(num1, num2, mult))
#Fim
print('Parabéns!!! você conseguiu! :)')