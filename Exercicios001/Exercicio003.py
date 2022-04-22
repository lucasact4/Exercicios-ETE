#Ex 1 = Descrição Narrativa
#Passo 1 - Obter a variável.
#Passo 2 - Mostrar e verificar a variável.
#Passo 3 - Se a variável for uma letra, então escreva “Você digitou uma letra”; caso contrário, escreva “Você digitou um número”.
#Ex 2 = Fluxograma
#Início > Recebimento de dados > Verificação da variável/dados > Resposta: Se letra-Sim|Se número-Não > Fim
#Ex 3 = Pseudocódigo
#Início
nome = input('Para começar, digite seu nome: ')
print('Eae {}? vamos dar início ao código ?'.format(nome))
#Passo 1 + Recebimento de dados
var1 = input('Digite uma variável: ')
#Passo 2 + Verificação da variável/dados
print('Você digitou o seguinte: {}!'.format(var1))
#Passo 3 + Resposta: Se letra-Sim|Se número-Não
print('Você digitou uma letra?', var1.isalpha())
print('Você digitou um número?', var1.isnumeric())
#Fim
print('Parabéns!!! você conseguiu! :)')