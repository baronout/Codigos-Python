#Codigo para comparar datas
from datetime import datetime

data1 = ""
data2 = ""
count1 = 1
count2 = 1
numero = 0

while count1 <= 3:
    numero = int(input("Insira dia, mês e ano da primeira data: "))
    if numero > 0: 
        data1 = data1+str(numero)
    count1 = count1+1

while count2 <= 3:
    numero = int(input("Insira dia, mês e ano da segunda data: "))
    if numero > 0: 
        data2 = data2+str(numero)
    count2 = count2+1

data1 = data1.rstrip("-")
data2 = data2.rstrip("-")

data_nova = datetime.strptime(data1,'%d, ')

print(data_nova)




