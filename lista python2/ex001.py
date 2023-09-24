numeros = [0,0]
maior = 0
for i in range(len(numeros)):
    numeros[i] = int(input("Digite um numero: "))
    if(numeros[i]>maior):
        maior = numeros[i]

print("Maior numero: "+str(maior))


'''
switch = math

a=1
math a:
    case 1:
        print("teste")
    case _:
        print("Default")
'''