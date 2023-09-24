salario = float(input("Digite seu salario: "))
aux = salario
aumento =0
valorAumento=0

if salario <=280:
    valorAumento = salario*0.20
    salario+= valorAumento
    aumento=20
elif salario>280 and salario<=700:
    valorAumento = salario*0.15
    salario+= valorAumento
    aumento=15
elif salario>700 and salario<=1500:
    valorAumento = salario*0.10
    salario+= valorAumento
    aumento = 10
else:
    valorAumento = salario*0.05
    salario+= valorAumento
    aumento=5

print("Salario antes do bonus: "+str(aux)+"\nDepois do bonus: "+str(salario)+"\nBonus: "+str(aumento)+"%"+"\nValor adicionado: "+str(valorAumento))