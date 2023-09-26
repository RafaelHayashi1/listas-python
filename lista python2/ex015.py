lados = [0,0,0]

for i in range(len(lados)):
    lados[i] = float(input("Digite um dos lados do triangulo: "))


if lados[0]+lados[1]>lados[2]:
    if lados[0]==lados[1] and lados[0]==lados[2]:
        print("Triângulo Equilátero")
    elif lados[0]==lados[1] or lados[0]==lados[2]:
        print("Triângulo Isósceles")
    else:
        print("Triango Escaleno")
