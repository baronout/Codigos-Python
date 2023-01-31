#Codigo para calcular media de numeros com começo e fim determinado

lista_total = []
lista_valida = []
n = 0
soma = 0

while n >= 0:
    n = int(input("Digite um número ou digita -1 para parar: "))
    if n>= 0:
        lista_total.append(n)

for x in lista_total:
    if x >= 25 and x <= 121 :
        lista_valida.append(x)
        soma = soma+x

media = int(soma/len(lista_valida))

resultado = "A media dos valores entre 25 e 121 é '{0}'."
print(resultado.format(media))
