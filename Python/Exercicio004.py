nomes = ['Para iniciarmos, siga os seguintes comandos na ordem correta:', '1. Decolar', '2. Função Piloto Automático', '3. Acelerar', '4. Pousar', '5. Planar']
for n in nomes:
  print(n)
er = ('Ação incorreta, tente novamente!')
m1 = float(input('Digite a primeira ação: '))
if m1 == 3:
  print('O avião está acelerando...')
elif m1 != 3:
  print(er)
  exit()
m2 = float(input('Digite a segunda ação: '))
if m2 == 1:
  print('O avião está decolando...')
elif m2 != 1:
  print(er)
  exit()
m3 = float(input('Digite a terceira ação: '))
if m3 == 5:
  print('O avião está planando...')
elif m3 != 5:
  print(er)
  exit()
m4 = float(input('Digite a quarta ação: '))
if m4 == 2:
  print('O avião está no Piloto Automático...')
elif m4 != 2:
  print(er)
  exit()
m5 = float(input('Digite a quarta ação: '))
if m5 == 4:
  print('O avião está Pousando...')
elif m5 != 4:
  print(er)
  exit()
print('Parábens, você conseguiu acertar a ordem correta!')
print('Resumo da ordem: \n3. Acelerar\n1. Decolar\n5. Planar\n2. Função Piloto Automático\n4. Pousar')