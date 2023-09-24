sexo = "kdkdkd"

while sexo != 'M' and sexo !='F':
    sexo = input("Digite seu sexo(M/F): ").upper()
    if sexo == 'M':
        print("Masculino")
    elif sexo=='F':
        print("Feminino")
    else:
        print("Sexo Inválido")
    