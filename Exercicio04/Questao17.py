h = 1
 
try:
 
    n = int(input("n = "))
 
    for c in range(2,n + 1):
 
        h += 1 / c
 
    print("H = %f" % h)
 
except:
 
    print("Não foi digitado um valor inteiro.")