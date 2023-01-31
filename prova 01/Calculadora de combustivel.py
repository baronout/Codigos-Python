#Código para calcular eficiencia de combustivel;
import math
tempo_viagem = int(input("Insira o tempo de viagem em segundos: "))
combus_gasto = int(input("Insira o combustivel gasto em litros: "))
combus_preco = float(input("Insira o preço do combustivel em R$: "))
distancia = int(input("Insira a distância percorrida em Km: "))

#Agora vamos calcular cada uma das métricas que o computador de bordo deve exibir;
veloc_media = math.ceil(distancia/(tempo_viagem/3600))
print("A velociade media durante a viagem foi de: ",veloc_media,"Km/H")

custo_viagem = round(combus_gasto*combus_preco,2)
print("O custo da viagem foi: R$", custo_viagem)

combus_custo = round(combus_preco/distancia,2)
print("O custo da viagem em R$/Km foi:", combus_custo)

combus_desemp = math.ceil(distancia/combus_gasto)
print("O desempenho do carro em Km/L foi: ",combus_desemp,"Km/L")

combus_tempo = round(combus_gasto/(tempo_viagem/3600),2)
print("O desempenho do carro em L/H foi: ",combus_tempo,"L/H")