div = 0
divi = 0
 
n = int(input("Digite um número inteiro: "))
 
if n > 0:
 
    for c in range(n,0,-1):
     
        if n % c == 0:
     
            div += 1
     
    if div > 2:
     
        print("%d não é um número primo." % n)
     
    else:
     
        print("%d é um número primo." % n)
 
elif n == 0:
 
    print("Zero não é um número primo.")
 
elif n < 0:
 
    for c in range(n,0,1):
 
        if n % c == 0:
 
            div += 1
 
    for c in range(1,abs(n) + 1,1):
 
        if n % c == 0:
 
            divv += 1
 
    if div + divi > 4:
 
        print("%d não é um número primo." % n)
 
    else:
 
        print("%d é um número primo." % n)