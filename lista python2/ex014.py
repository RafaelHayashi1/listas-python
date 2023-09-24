notas =[0,0]
conceito = 'L'
media = 0
resultado = 'd'
for i in range(len(notas)):
    notas[i] = float(input("Digite uma nota: "))
    media+=notas[i]

media /=len(notas)

if media>=9 and media<=10:
    conceito ='A'
elif media<=9 and media >=7.5:
    conceito = 'B'
elif media<=7.5 and media >=6:
    conceito = 'C'
elif media<=6 and media >=4:
    conceito = 'D'
else:
    conceito = 'F'


if conceito =='A' or conceito=='B' or conceito=='C':
    resultado='Aprovado'
else:
    resultado='Reprovado'

print("Nota 1: "+str(notas[0])+"\nNota 2: "+str(notas[1])+"\nMédia: "+str(media)+"\nConceito: "+str(conceito)+"\nResultado: "+str(resultado))