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
        max=num
    else:
        if num<oculto:
            min=num
    print("Você errou! o numero está entre",min,"e",max)
    tentativas = tentativas+1
    num = int(input("Insira um numero: "))
print("Acertou!!!!!")
print("Você acertou em",tentativas,"tentativas")