try:

	b = int(input("Digite dois valores inteiros para 'b' e 'n': "))
	n = int(input())

	while b < 2 or n <= 1:

		try:

			b = int(input("Digite dois valores inteiros para 'b' e 'n': "))
			n = int(input())

		except:

			print("Não foram digitados valores inteiros.")

	print("'b' elevado a 'n' é %d." % pow(b, n))

except:

	print("Não foram digitados valores inteiros.")