import random

#Código para gerar um numero aleatório e fazer com que o usuario adivinhe ele;

#Vamos declarar o range máximo que o nosso numero pode ter e gerar um aleatório;

min = 1
max = 1000
oculto = random.randint(min,max)
tentativas = 0

#Agora vamos pedir que o usuario tente adivinhar e dar algumas dicas para ele;
num = int(input("Insira um numero: "))
while num != oculto:
    if num>oculto:
        print("Está abaixo deste numero!")
    else:
        if num<oculto:
            print("Está acima deste numero!")
    num = int(input("Insira um numero: "))
print("Acertou!!!!!")