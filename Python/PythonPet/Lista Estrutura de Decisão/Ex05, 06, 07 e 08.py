# 5. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# 6. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# 7. A mensagem "Reprovado", se a média for menor do que sete;
# 8. A mensagem "Aprovado com Distinção", se a média for igual a dez.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 7:
    print(f'REPROVADO.\nNota: {media:.1f}')
elif media == 10:
    print(f'APROVADO COM DISTINÇÃO.\nNota: {media:.1f}')
elif media >= 7:
    print(f'APROVADO.\nNota: {media:.1f}')
