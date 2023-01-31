#Calculadora de tempo de estacionamento;

tempo = int(input("Insira o tempo em minutos: "))
tempo = round(tempo/60,1)

if tempo > 0 and tempo <= 1 :
    print("O total a pagar é: R$",tempo*8)
elif tempo > 1 and tempo <= 2 :
    print("O total a pagar é: R$",tempo*8)
elif tempo > 2 and tempo <= 3 :
    print("O total a pagar é: R$",16+tempo*)