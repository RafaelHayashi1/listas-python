
import math
import sys
valores = [0,0,0]

for i in range (len(valores)):
    valores[i] = float(input("Digite um valor: "))
    if valores[0] == 0:
        print("Equacão não é de segundo grau.")
        sys.exit()


'''Calcular Delta'''
try:
    delta = math.sqrt((valores[1]**2 - 4 * valores[0] * valores[2])) 
except:
    print("A equação não possui raizes")
    sys.exit()



if delta==0:
    print("A equação só possui uma raiz real")
    raiz = -valores[1] / (2*valores[0])    
    print("Raiz: "+str(raiz))   
else:
    print("A equação possui duas raiz reais")  
    raiz1 = -valores[1] / (2*valores[0])
    raiz2 = +valores[1] / (2*valores[0])   
    print("Raiz 1: "+str(raiz1)+"\nRaiz 2: "+str(raiz2))







