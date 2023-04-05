def numeros(lista):
    for num in lista:
        if num % 2 == 0:
            return False
    return True

def pegar_numeros():
    lista = []
    while True:
        num = int(input("Insira os valores que deseja colocar na lista(Digite -1 para parar): "))
        if num < 0:
            break
        lista.append(num)
    return lista

lista = pegar_numeros()
print(numeros(lista))
