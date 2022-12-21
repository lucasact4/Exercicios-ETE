# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
  sexo = input("Digite o seu Sexo: [F/M]").upper()
  if sexo == "F" or sexo == "M":
    break
  else:
    print("Sexo inválido!")
if sexo == "F":
  print("Feminino!")
else:
  print("Masculino!")
  