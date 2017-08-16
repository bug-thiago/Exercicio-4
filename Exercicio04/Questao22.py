def Euclides(a, b):
    
    if b == 0:
        
        return a
    
    else:
        
        return euclides(b, a % b)
 
a, b = int(input("Digite dois números inteiros positivos: ")), int(input())

if a > 0 and b > 0:


	print("O MDC entre %d e %d é %d." % (a, b, Euclides(a, b)))

else:

	print("Erro: é preciso que dois números inteiros e positivos sejam fornecidos.")