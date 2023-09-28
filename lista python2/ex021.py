valor = 0
while valor < 10 or valor > 600:
    valor = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

notas = [0, 0, 0, 0, 0]  #  [100, 50, 10, 5, 1]

while valor >= 100:
    valor -= 100
    notas[0] += 1

while valor >= 50:
    valor -= 50
    notas[1] += 1

while valor >= 10:
    valor -= 10
    notas[2] += 1

while valor >= 5:
    valor -= 5
    notas[3] += 1

while valor >= 1:
    valor -= 1
    notas[4] += 1

print("Quantidade de notas de 100 reais:", notas[0])
print("Quantidade de notas de 50 reais:", notas[1])
print("Quantidade de notas de 10 reais:", notas[2])
print("Quantidade de notas de 5 reais:", notas[3])
print("Quantidade de notas de 1 real:", notas[4])
