B# Exercício
pessoas = [ ]
idades = [ ]
for p in range (0, 5):
  print('Pessoa: ', p+1)
  pessoa = input('Digite o nome de alguém: ')
  idade = int(input('Agora digite a idade: '))
  idades.append(idade)
  pessoas.append(pessoa)
print(pessoas, idades)