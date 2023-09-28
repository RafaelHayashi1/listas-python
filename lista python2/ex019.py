valor = 0
contadorCentena =0
contadorDezena = 0
contadorUnidade =0
while valor < 1 or valor > 1000:
    valor = int(input("Digite um numero de 1-1000: "))


while valor >= 100:
    valor-=100
    contadorCentena+=1

while valor <100 and valor>=10:
    valor-=10
    contadorDezena+=1

while valor >0 and valor<=10:
    valor-=1
    contadorUnidade+=1


print("Centenas: "+str(contadorCentena))
print("Dezenas: "+str(contadorDezena))
print("Unidades: "+str(contadorUnidade))
