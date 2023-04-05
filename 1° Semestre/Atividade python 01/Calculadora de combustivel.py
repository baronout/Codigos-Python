#Código para calcular eficiencia de combustivel;
import math
tempo_viagem = int(input("Insira o tempo de viagem em minutos: "))
combus_gasto = int(input("Insira o combustivel gasto em litros: "))
combus_preco = float(input("Insira o preço do combustivel em R$: "))
distancia = int(input("Insira a distância percorrida em Km: "))

#Calculo para a velocidade média;
veloc_media = math.ceil(distancia/(tempo_viagem/60))
print("A velocidade media durante a viagem foi de: ",veloc_media,"Km/H")

#Calculo para o custo da viagem;
custo_viagem = round(combus_gasto*combus_preco,2)
print("O custo da viagem foi: R$", custo_viagem)

#Custo da viagem por km;
combus_custo = round(combus_preco/distancia,2)
print("O custo da viagem em R$/Km foi:", combus_custo)

#Desempenho do carro por km/l;
combus_desemp = math.ceil(distancia/combus_gasto)
print("O desempenho do carro em Km/L foi: ",combus_desemp,"Km/L")

#Desempenho do carro em l/h;
combus_tempo = round(combus_gasto/(tempo_viagem/60),2)
print("O desempenho do carro em L/H foi: ",combus_tempo,"L/H")