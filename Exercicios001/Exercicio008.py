nomes = ['Para iniciarmos, siga os seguintes comandos na ordem correta:', '1. Decolar', '2. Função Piloto Automático', '3. Acelerar', '4. Pousar', '5. Planar']
for n in nomes:
  print(n)
er = ('Ação incorreta, tente novamente!')
mm = []
m2 = ''
while m2 != 'Acelerar':
  m2 = input("Digite a primeira ação que deve ser feita: ")

  if m2 != "Acelerar":
    print("Ação incorreta, tente novamente!")

  mm.append(m2)

print("Acelerando...")
#  print(er)
#  print('Parábens, você conseguiu acertar a ordem correta!')
#  print('Resumo da ordem: \n3. Acelerar\n1. Decolar\n5. Planar\n2. Função Piloto Automático\n4. Pousar')