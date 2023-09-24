'''  
1 litro = 6 metros quadrados
tinta vendida em latas de 18 litros = 80
1 lata 18 litros = 108 metros quadrados
1 lata 3,6 litros = 21,6 = 25
'''
import math
metrosQuadrados = float(input("Digite o tamanho em metros quadrados da area desejada: "))

'''
Folga de 10%
'''
quantidade_de_tinta_litros = metrosQuadrados*1.1 / 6



quantidade_latas_18_litros = math.ceil(quantidade_de_tinta_litros / 18)
quantidade_galoes_3_6_litros = math.ceil(quantidade_de_tinta_litros / 3.6)

precoLatas18 = quantidade_latas_18_litros*80
precoGalao3_6 = quantidade_galoes_3_6_litros*25


quantidade_latas_misturadas = int(quantidade_de_tinta_litros // 18)
resto_tinta_misturada = quantidade_de_tinta_litros % 18
quantidade_galoes_misturados = math.ceil(resto_tinta_misturada / 3.6)

preco_total_misturado = (quantidade_latas_misturadas * 80) + (quantidade_galoes_misturados * 25)

print("Apenas Latas de 18 Litros:")
print("Latas: " + str(quantidade_latas_18_litros))
print("Preço: R$ " + str(precoLatas18))

print("\nApenas Galões de 3,6 Litros:")
print("Galões: " + str(quantidade_galoes_3_6_litros))
print("Preço: R$ " + str(precoGalao3_6))

print("\nMisturando Latas e Galões:")
print("Latas: " + str(quantidade_latas_misturadas))
print("Galões: " + str(quantidade_galoes_misturados))
print("Preço: R$ " + str(preco_total_misturado))








