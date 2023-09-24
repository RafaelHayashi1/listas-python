numeros = [0,0,0]
maior = 0
for i in range(len(numeros)):
    numeros[i] = int(input("Digite um numero: "))
    if(numeros[i]>maior):
        maior = numeros[i]