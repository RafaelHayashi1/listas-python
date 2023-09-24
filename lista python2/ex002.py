condicao = 'aA'

while condicao !='S':
    numero = int(input("Digite um numero: "))
    if(numero>0):
        print("Seu numero é positivo.")
    else:
        print("Seu numero é negativo.")

    condicao = input("Deseja parar(S=Parar/N=Continuar): ").upper()
