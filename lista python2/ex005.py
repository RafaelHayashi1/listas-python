notas = [0,0]
media =0
for i in range(len(notas)):
    notas[i] = float(input("Digite sua nota: "))
    media+=notas[i]

media /=len(notas)
print(media)