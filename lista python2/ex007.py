numeros = [0,0,0]
maior = 0
menor = 44
for i in range(len(numeros)):
    numeros[i] = int(input("Digite um numero: "))
    if(numeros[i]>maior):
        maior = numeros[i]
    if(numeros[i]<menor):
        menor = numeros[i]

print("Maior numero: "+str(maior))
print("Menor numero: "+str(menor))
