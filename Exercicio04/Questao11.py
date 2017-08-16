a = 5000000
b = 7000000

anos = 0

while a != b:

	a += 5000000 * 0.03
	b += 7000000 * 0.02

	anos += 1

print("Serão necessários %d anos." % anos)