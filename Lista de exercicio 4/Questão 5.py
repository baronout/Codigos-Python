#Codigo para descobrir a menor potencia equivalente ao numero inserido

numero = int(input("Digite um numero: "))
resultado = 0

while resultado < numero:
    for x in range(0,numero):
        potencia = 2**x
        resultado = potencia
        if resultado > numero:
            break
resposta = "O numero anterior a menor potencia de base dois do numero {0} é {1}"
print(resposta.format(numero,resultado-1))



