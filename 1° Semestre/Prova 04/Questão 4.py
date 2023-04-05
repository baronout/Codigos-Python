lista = []
numero = 0 

# Loop para inserir números na lista
while numero >= 0:
    numero = int(input("Insira um número que deseja adicionar à lista (Insira -1 para parar):"))
    if numero >= 0:
        lista.append(numero)

# Cria duas listas, uma com números pares e outra com números ímpares
lista_par = [x for x in lista if x % 2 == 0]
lista_impar = [x for x in lista if x % 2 != 0]

# Ordena as listas de números pares e ímpares
lista_par.sort()  
lista_impar.sort()  

termos = 1
segmento = []
contador_segmento = 0

# Loop para criar segmentos da lista
while len(lista_par) > 0 or len(lista_impar) > 0:
    segmento = []  # inicializa um novo segmento
    if len(lista_par) > 0:
        segmento.append(lista_par.pop(0))  # adiciona o próximo número par
    elif len(lista_impar) > 0:
        segmento.append(lista_impar.pop(0))  # adiciona o próximo número ímpar

    # Adiciona termos ao segmento
    for i in range(termos - 1):
        if len(lista_par) > 0 and len(lista_impar) > 0:
            # Verifica se o próximo número a ser adicionado é par ou ímpar
            if (segmento[0] % 2 == 0 and lista_impar[0] % 2 != 0) or (segmento[0] % 2 != 0 and lista_par[0] % 2 == 0):
                segmento.append(lista_par.pop(0) if segmento[0] % 2 == 0 else lista_impar.pop(0))
        elif len(lista_par) > 0:
            segmento.append(lista_par.pop(0))
        elif len(lista_impar) > 0:
            segmento.append(lista_impar.pop(0))

    print(segmento)  # imprime o segmento atual
    contador_segmento = contador_segmento + len(segmento)
    termos = termos + 1

# Verifica se a lista é piramidal
if contador_segmento != len(lista):  
    print("A sequência não é piramidal")
else:
    print("A sequência é piramidal")
