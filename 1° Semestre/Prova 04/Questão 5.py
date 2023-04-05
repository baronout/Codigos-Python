import json

def carregar_dados(): # Função para carregar dados de um arquivo .json
    try: # Tenta abrir o arquivo "dados.json" para leitura
        with open("dados.json", "r") as arquivo: 
            dados = json.load(arquivo) # Carrega os dados do arquivo e armazena em uma variável
    except FileNotFoundError: # Caso o arquivo não seja encontrado, cria um dicionário vazio
        dados = {}
    return dados # Retorna os dados carregados ou o dicionário vazio

def salvar_dados(dados): #
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo) #Salva os dados em formato JSON, para facilitar a leitura

def cadastrar_cpf(dados):
    cpf = input("Digite o CPF: ")
    if cpf in dados: # Vrifica no arquivo de dados se o CPF já existe nele, se sim, retorna essa mensagem
        print("CPF já cadastrado.")
    else:
        dados[cpf] = [] # Caso não tenha, é adicionado o novo CPF
        print("CPF cadastrado com sucesso.")

def remover_cpf(dados):
    cpf = input("Digite o CPF: ")
    if cpf in dados:
        del dados[cpf] # Remove o CPF do arquivo de dados
        print("CPF removido com sucesso.")
    else:
        print("CPF não cadastrado.") # Caso não exista o dado no arquivo, este erro é retornado

def adicionar_mac(dados):
    cpf = input("Digite o CPF: ")
    if cpf in dados: # Só é possivel adicionar um MAC, se antes houver um CPF cadastrado para que seja possivel associar os dois
        mac = input("Digite o MAC: ")
        dados[cpf].append(mac) # É criado uma sublista com o CPF e MACs juntos dele
        print("MAC adicionado com sucesso.")
    else:
        print("CPF não cadastrado.")

def remover_mac(dados):
    cpf = input("Digite o CPF: ")
    if cpf in dados: # Como os MACs são organizados por CPF, podemos guardar mais de 1 MAC e assim podemos apagar qualquer um deles também
        mac = input("Digite o MAC: ")
        if mac in dados[cpf]:
            dados[cpf].remove(mac)
            print("MAC removido com sucesso.")
        else:
            print("MAC não encontrado.")
    else:
        print("CPF não cadastrado.")

def listar_cpfs(dados):
    if len(dados) > 0:
        print("CPFs cadastrados:") # Lista todos os CPFs cadastrados no arquivo de dados
        for cpf in dados:
            print(cpf)
    else:
        print("Não há CPFs cadastrados.")

def listar_macs(dados):
    cpf = input("Digite o CPF: ")
    if cpf in dados: # Lista todos os MACs de acordo com o CPF cadastrado
        if len(dados[cpf]) > 0:
            print("MACs vinculados ao CPF {}:".format(cpf))
            for mac in dados[cpf]: # Procura e imprime todos os MACs listados para o CPF informado
                print(mac)
        else:
            print("Não há MACs vinculados ao CPF.")
    else:
        print("CPF não cadastrado.")

dados = carregar_dados() # Carrega os dados salvos no arquivo JSON

def menu():
    print("1 - Cadastrar CPF")
    print("2 - Remover CPF")
    print("3 - Adicionar MAC")
    print("4 - Remover MAC")
    print("5 - Listar CPFs")
    print("6 - Listar MACs")
    print("0 - Sair")

def iniciar_sistema():
    while True: # Seleciona as opções do menu
        menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_cpf(dados)
        elif opcao == 2:
            remover_cpf(dados)
        elif opcao == 3:
            adicionar_mac(dados)
        elif opcao == 4:
            remover_mac(dados)
        elif opcao == 5:
            listar_cpfs(dados)
        elif opcao == 6:
            listar_macs(dados)
        elif opcao == 0:
            salvar_dados(dados)
            break
        else:
            print("Opção inválida.") # Caso seja inserido um numero diferente dos listado

iniciar_sistema()