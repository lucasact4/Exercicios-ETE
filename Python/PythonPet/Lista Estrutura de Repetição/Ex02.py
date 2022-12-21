# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
print("Cadastro:")
usuario = input("Usuário: ")
senha = input("Senha: ")
while usuario==senha:
	print("ERRO: O usuário não pode ser igual a senha, tente novamente!")
	usuario = input("Usuário: ")
	senha = input("Senha: ")
else:
	print("Cadastrado efetuado com sucesso!")
    