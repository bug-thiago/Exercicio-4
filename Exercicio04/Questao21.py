def fib(n):

	a, b = 1, 1

	for c in range(n - 1):

		a, b = b, a + b

	return a

n = int(input("F"))

if n > 0:

	print(fib(n))

else:

	print("É preciso fornecer um valor positivo.")