#Calculadora de dias do ano

#Inserindo as datas;
dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))

#Calculando o numero do dia do ano, somando o dia com a quantidade de dias que já passaram;
if ano%4 == 0  :
    if mes == 1 :
        print(dia,"/",mes,"/",ano)
    elif mes == 2 :
        print(dia,"/",mes,"/",ano," É o dia",dia+31)
    elif mes == 3 :
        print(dia,"/",mes,"/",ano," É o dia",dia+60)
    elif mes == 4 :
       print(dia,"/",mes,"/",ano," É o dia",dia+91) 
    elif mes == 5 :
        print(dia,"/",mes,"/",ano," É o dia",dia+121)
    elif mes == 6 :
        print(dia,"/",mes,"/",ano," É o dia",dia+152)
    elif mes == 7 :
        print(dia,"/",mes,"/",ano," É o dia",dia+182)
    elif mes == 8 :
        print(dia,"/",mes,"/",ano," É o dia",dia+213)
    elif mes == 9 :
        print(dia,"/",mes,"/",ano," É o dia",dia+244)
    elif mes == 10 :
        print(dia,"/",mes,"/",ano," É o dia",dia+274)
    elif mes == 11 :
        print(dia+304,"/",mes,"/",ano," É o dia",dia+305)
    elif mes == 12 :
        print(dia,"/",mes,"/",ano," É o dia",dia+335)
else :
    if mes == 1 :
        print(dia,"/",mes,"/",ano)
    elif mes == 2 :
        print(dia,"/",mes,"/",ano," É o dia",dia+31)
    elif mes == 3 :
        print(dia,"/",mes,"/",ano," É o dia",dia+59)
    elif mes == 4 :
       print(dia,"/",mes,"/",ano," É o dia",dia+90) 
    elif mes == 5 :
        print(dia,"/",mes,"/",ano," É o dia",dia+120)
    elif mes == 6 :
        print(dia,"/",mes,"/",ano," É o dia",dia+151)
    elif mes == 7 :
        print(dia,"/",mes,"/",ano," É o dia",dia+181)
    elif mes == 8 :
        print(dia,"/",mes,"/",ano," É o dia",dia+212)
    elif mes == 9 :
        print(dia,"/",mes,"/",ano," É o dia",dia+243)
    elif mes == 10 :
        print(dia,"/",mes,"/",ano," É o dia",dia+273)
    elif mes == 11 :
        print(dia+304,"/",mes,"/",ano," É o dia",dia+304)
    elif mes == 12 :
        print(dia,"/",mes,"/",ano," É o dia",dia+334)