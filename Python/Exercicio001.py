#Exercicio
dado1 = list()
dado2 = list()
p = 0
print('-='*5, 'Organizador de idades', '-='*5)
for c in range (0, 5):
        dado1.append(str(input('Digite o nome do participante: ')))
        dado2.append(int(input('Digite a idade agora: ')))
print('-='*5, 'Nomes dos participantes', '-='*5)
print(dado1)
print('-='*5, 'Idades respectivas', '-='*5)
print(dado2)
print('-='*30)
dado2.sort(reverse=True)
print('-='*5, 'Idades de forma decrescentes', '-='*5)
print(dado2)