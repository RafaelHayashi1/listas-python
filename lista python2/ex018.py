def data_valida(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        return 1 <= mes <= 12 and 1900 <= ano <= 2100 and 1 <= dia <= (29 if mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) else 30 if mes in [4, 6, 9, 11] else 31)
    except ValueError:
        return False

data = input("Digite uma data no formato dd/mm/aaaa: ")

if data_valida(data):
    print("A data é válida.")
else:
    print("A data é inválida.")
