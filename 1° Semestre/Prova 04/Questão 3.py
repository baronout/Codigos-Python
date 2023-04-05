def lista_mesmo_tamanho(list):
    resultado = [] # Inicializa a lista que armazenará as sublistas
    lista_atual = [] # Inicializa a lista atual que será adicionada à lista 'resultado'
    tamanho_atual = 1 # Inicializa o comprimento da lista atual como 1
    for num in list: # Loop por todos os elementos na lista 'list'
        if num == -1: # Se o elemento for -1, saia do loop
            break
        lista_atual.append(num)  # Adicione o elemento atual à lista atual
        if len(lista_atual) == tamanho_atual: # Se o comprimento da lista atual é igual ao comprimento desejado
            resultado.append(lista_atual) # Adicione a lista atual à lista 'resultado'
            lista_atual = [] # Reinicie a lista atual
            tamanho_atual += 1 # Aumente o comprimento desejado da lista atual
    return resultado

def numeros():
    lista = [] # Inicializa a lista
    while True: # Loop até que o usuário insira -1
        num = int(input("Insira os valores que quer adicionar a lista (Insira -1 para parar): ")) # Obtenha um número do usuário
        if num == -1: # Se o número for -1, saia do loop
            break
        lista.append(num) # Adicione o número à lista
    return lista

lista_todos = numeros() # Obtenha a lista do usuário
print(lista_mesmo_tamanho(lista_todos)) # Imprima a lista de listas resultante
