# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe um nome: ")
while ( len(nome) <=  3 ):
	nome = input("Informe um nome: ")

idade = int(input("Informe a idade: "))
while ( idade > 150 or idade < 0 ):
	idade = int(input("Informe a idade: "))
	
salario = float(input("Informe um salário: "))
while ( salario < 0 ):
	salario = float(input("Informe um salário: "))

sexo = input("Informe a inicial do seu sexo: [M/F]").upper()
while  sexo !="F" and sexo!="M" :
	sexo = input("Informe a inicial do seu sexo: [M/F]").upper()

estado_civil = input("Informe a inicial do seu estado civil: [S-Solteiro/C-Casado/V-Viúvo/D-Divorciado]").upper()
while ( estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D" ):
	estado_civil = input("Informe a inicial do seu estado civil: ").upper()
    