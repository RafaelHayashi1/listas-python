'''  
1 litro = 3 metros quadrados
tinta vendida em latas de 18 litros = 80
1 lata = 54 metros quadrados
'''

metrosQuadrados = float(input("Digite o tamanho em metros quadrados da area desejada: "))
latas = 3/(metrosQuadrados/18)
precoLatas = latas *80
print("Quantidade de Latas: "+str(latas)+"\nPreco: "+str(precoLatas))
