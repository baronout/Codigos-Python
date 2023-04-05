valor = int(input("Insira um valor: "))

if valor > 0 :
    if valor %2 == 0 :
        print("O valor é positivo e par!!!")
    else :
        print("O valor é positivo e ímpar!!!")
elif valor < 0 :
    if valor %2 == 0 :
        print("O valor é negativo e par!!!")
    else :
        print("O valor é negativo e ímpar!!!")
else :
    print("O valor é nulo")