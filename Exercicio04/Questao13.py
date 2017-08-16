y = []
soma = 0

x = int(input("Digite números inteiros e positivos (0 para sair): "))

if x == 0:

	pass

else:
 
	while x != 0:
	 
	    if x == 0:
	 
	        break
	 
	    x = int(input())
	 
	    if x % 3 == 0:
	 
	        y.append(x)
	 
	for c in range(len(y)):
	 
	    soma += y[c]
	 
	print("A média dos números múltiplos de três dentre os Digitados  é: %d" % (soma / int(len(y) - 1)))
