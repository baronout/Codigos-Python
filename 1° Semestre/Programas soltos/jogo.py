import random
palavras = ["ROMA","NATAL","BELEM", "RICHARLISSON", "NEYMAR"]
oculto = random.choice(palavras)
exibida = "_"*len(oculto)
tentativas = 0
print(exibida)

while exibida != oculto and tentativas != int(len(oculto)*2):
    letra = input("Insira uma letra: ").upper()
    tentativas = tentativas+1
    if tentativas != int(len(oculto)*2):
        aExibir = ""
        for pos in range(len(oculto)):
            if oculto[pos] == letra:
                aExibir += letra
            else:
                    aExibir += exibida[pos]
        print(aExibir)
        print("Total de tentativas", tentativas)
        exibida = aExibir
        if exibida == oculto:
            print("Você conseguiu!!!")
ultima_tentativa = input("Ultima tentativa, digite a palavra inteira!!: ")

print("Você ultrapassou as chances", tentativas)