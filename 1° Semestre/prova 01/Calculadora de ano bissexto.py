#Calculadora de ano bissexto;

ano = int(input("Insira o ano: "))

if ano%4 == 0 :
    print("Ano bissexto")
else :
    print("Não é bissexto")