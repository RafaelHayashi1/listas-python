horas = float(input("Digite quantas horas vc trabalha por mes: "))
salarioh = float(input("Digite o salario por hora que vc ganha: "))
total = horas*salarioh
totalIR = total*0.11
totalINSS = total*0.08
totalSINDICATO = total * 0.05
resultado = total-(totalSINDICATO+totalINSS+totalIR)


print("Salario Bruto: "+ str(total) +"\nIR: " + str(totalIR)+ "\nINSS: "+str(totalINSS) + "\n10SINCICATO: "+str(totalSINDICATO) + "\nSALARIO Liquido:"+ str(resultado) )

