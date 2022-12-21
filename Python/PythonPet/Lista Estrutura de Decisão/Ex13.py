# 13. Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
while True:
  turno = input("Digite o seu turno:\n[M-Matutino] [V-Vespertino] [N-Noturno]").upper()
  if turno == "M" or turno == "V" or turno == "N":
    break
  else:
    print("Valor inválido!\nTente novamente!")
if turno == "M":
  print("Bom dia!")
elif turno == "V":
  print("Boa tarde!")
else:
  print("Boa noite!")
  