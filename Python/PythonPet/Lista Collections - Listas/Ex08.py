# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
vh = float(input("Digite o valor ganho por hora de trabalho: "))
ht = float(input("Digite o valor de horas trabalhadas neste mês: "))
pay = vh * ht
print(f"O pagamento que deve ser recebido é de: R${pay}")
