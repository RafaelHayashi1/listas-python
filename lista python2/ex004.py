letra = input("Digite uma letra: ").upper()
vogais = ['A','E','I','O','U']

if letra in vogais:
    print("Vogal:"+ letra)
else:
    print("Consoante:"+ letra)
