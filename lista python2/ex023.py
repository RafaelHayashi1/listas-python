numero = float(input("Digite um número: "))

numero_arredondado = round(numero)

if numero == numero_arredondado:
    print("O número é um número inteiro.")
else:
    print("O número  é um número decimal.")
