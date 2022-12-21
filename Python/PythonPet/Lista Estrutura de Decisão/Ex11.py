# 11. Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
n1 = int(input('Digite o preço do PRIMEIRO produto R$'))
n2 = int(input('Digite o preço do SEGUNDO produto R$'))
n3 = int(input('Digite o preço do TERCEIRO produto R$'))
menor = n1
produto = "PRIMEIRO"
if n2 < n1 and n2 < n3:
    menor = n2
    produto = "SEGUNDO"
elif n3 < n1 and n3 < n2:
    menor = n3
    produto = "TERCEIRO"
print(f'Você deve comprar o {produto} produto por custar R${menor} e ser mais barato que os restantes!')
