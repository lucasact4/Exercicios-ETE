# 5. Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
populaçãoA = float(input("Informe a população da cidade A: "))
populaçãoB = float(input("Informe a população da cidade B: "))
ano=0
taxa_crescimentoA = float(input("Informe a taxa de crescimento da população da cidade A: "))
taxa_crescimentoB = float(input("Informe a taxa de crescimento da população da cidade B: "))

while populaçãoA < populaçãoB:
	populaçãoA+=round((populaçãoA*taxa_crescimentoA)/100)
	populaçãoB+=round((populaçãoB*taxa_crescimentoB)/100)
	ano=ano+1

print(f"Levará {ano} anos para população da cidade A ser maior que a cidade B")
print(f"populaçãoB: {populaçãoB} habitantes")
print(f"populaçãoA: {populaçãoA} habitantes")
