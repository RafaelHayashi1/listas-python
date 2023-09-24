valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.1
else:
    desconto_ir = salario_bruto * 0.2

if salario_bruto <= 1000:
    desconto_inss = salario_bruto * 0.08
else:
    desconto_inss = salario_bruto * 0.1

fgts = salario_bruto * 0.11

salario_liquido = salario_bruto - desconto_ir - desconto_inss 


print("Folha de Pagamento")
print("Salário Bruto: R$ "+str(salario_bruto))
print("Desconto IR: R$ "+str(desconto_ir))
print("Desconto INSS: R$ "+str(desconto_inss))
print("FGTS: R$ "+str(fgts))
print("Salário Líquido: R$ "+str(salario_liquido))
