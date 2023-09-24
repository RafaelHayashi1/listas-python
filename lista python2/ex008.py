precoProdutos = [0,0,0]
menor = 160070
for i in range(len(precoProdutos)):
    precoProdutos[i] = float(input("Digite o preco do produto: "))
    if precoProdutos[i]<menor:
        menor = precoProdutos[i]
    
print("Preco: "+str(menor))