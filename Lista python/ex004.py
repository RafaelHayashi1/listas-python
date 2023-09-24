notas = [0,0,0,0,]
media = 0
for i in range(4):
    notas[i]= float(input("Digite as notas:"))
    media += notas[i]


print("Sua média é: "+str(media/4))