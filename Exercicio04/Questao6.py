u = input("Digite um nome de usuário e a sua respectiva senha (não podem ser iguais):\nUsername: ")
p = input("Senha: ")

while u == p:

	u = input("Erro: os valores não podem ser iguais.\nUsername: ")
	p = input("Senha: ")