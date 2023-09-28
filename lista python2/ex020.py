notas = [0,0,0]
soma =0
for i in range(len(notas)):
    notas[i] = float(input("Digite a nota: "))
    soma +=notas[i]

soma/=len(notas);


if soma == 10:
    print("Aprovado com Distinção: "+str(soma))
elif soma >= 7:
    print("Aprovado com média: "+str(soma))
else:
    print("Reprovado com média: "+str(soma))
