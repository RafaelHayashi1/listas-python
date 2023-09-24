n1=[0,0]
for i in range(2):
    n1[i]=int(input("Digite um numero inteiro: "))

n2 = float(input("Digite um numero real: "))



quest1 = n1[0] *2 + n1[1]/25
quest2 = n1[0] *3 + n2
quest3 =  n2**3


print("o produto do dobro do primeiro com metade do segundo: "+str(quest1)+"\na soma do triplo do primeiro com o terceiro: "+ str(quest2) +"\no terceiro elevado ao cubo: " + str(quest3))


