x = []

for c in range(100):

	x.append(int(input("X[%d] = " % c)))

x.sort()

print("\n%d" % x[99]) 