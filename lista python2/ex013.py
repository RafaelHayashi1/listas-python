condi = "kdakwdkwa"

while condi !="X":
    diaSemana = input("Digite um dia da semana(D-S-T-Q-QI-SE-SB): ").upper()
    if diaSemana=='D':
        print("Domingo")
    elif diaSemana=='S':
        print("Segunda")
    elif diaSemana=='T':
        print("Terça")
    elif diaSemana=='Q':
        print("Quarta")
    elif diaSemana=='QI':
        print("Quinta")
    elif diaSemana=='SE':
        print("Sexta")
    elif diaSemana=='X':
        condi='X'
    else:
        print("Sabado")
print("Fim")