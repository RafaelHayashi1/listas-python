contador = 0
pesos = []
execesso = 0
resultado = 0
while(contador!=99):
    peso = float(input("Digite o peso do peixe: "))
    pesos.append(peso)
    continuar = input("Deseja continuar inserindo dados?(S/N)")
    contador+=1
    if(continuar =='N' or continuar=='n'):
        contador=99;

quantidadePeixes = len(pesos)

for i in range(quantidadePeixes):
    if(pesos[i]>50):
        execesso+= pesos[i]-50

resultado = execesso*4


input("Taxa sobre os peixes: "+str(resultado))