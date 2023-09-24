temperaturaGF = float(input("Digite a temperatura em graus FR:"))
temperaturaGC = (5 * (temperaturaGF-32) / 9)
temperaturaGC = round(temperaturaGC)

print("Temperatura em GC: "+str(temperaturaGC))