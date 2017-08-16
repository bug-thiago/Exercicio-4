try:

	nota = float(input("Digite uma nota : "))

except:

	print("Não foi digitado um valor real.")

	nota = 1

while nota < 0 or nota > 10:

	try:

		nota = float(input("Erro! Digite uma nota válida (entre 0 e 10): "))

	except:

		print("Não foi digitado um valor real.")