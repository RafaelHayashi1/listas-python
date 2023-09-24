altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo(M OU F): ")
pesoIdeal = 0
if sexo == "M" or "m":
    pesoIdeal = (72.7*altura) - 58 
elif sexo == 'F' or 'f':
    pesoIdeal= (62.1*altura) - 44.7 
 


print("Seu peso ideal é: "+str(pesoIdeal))