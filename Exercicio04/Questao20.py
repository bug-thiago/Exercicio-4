y = []
soma = 0

print("Digite números inteiros (0 para sair): ")

x = int(input())

if x == 0:

	pass

else:

	y.append(x)

	while x != 0:

		if x == 0:

			break

		x = int(input())

		y.append(x)

	for c in range(len(y)):

		soma += y[c]

	print("A soma dos números digitados é %d. " % soma)