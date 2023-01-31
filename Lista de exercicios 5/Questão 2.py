import requests
import json

nome = input("Insira o seu nome completo: ") #Vamos iniciar coletando algumas informações básicas do usuario;
cep = input("Insira o seu CEP: ") #Dado importante para adquirir endereço e etc;
numero_casa = input("Insira o numero da sua casa: ")
informacoes = [] #Aqui vamos reunir todas as informações que coletamos em uma lista, para exibirmos no final;

def abrevia(nome): #Função para abreviar qualquer frase que quisermos;
    p = 0
    while len(nome)-len(numero_casa) > 35: #Parametro para especificar o tamanho máximo que nossa frase pode estar;
        palavras = [''] #Declarei a variavel palavra como uma lista vazia, para que não houvesse problemas quanto a declaração dela;
        palavras = nome.split() #Vamos separar a frase que obtivemos em varias sub-strings;
        if len(palavras[p]) > 3: #Aqui vamos colocar a quantidade minima de letras para que seja possivel abreviar, para salvar os casos de "e", "de" e "dos";
            palavras[p] = palavras[p][0].upper() + "." #Vamos substituir a palavra da vez, pela primeira letra da palavra junto de um ponto, caso ela esteja minuscula, já resolvemos também;
            nome = " ".join(palavras) #Juntamos as sub-strings em uma unica string novamente e vamos checar se ela tem 35 ou mais caracteres;
        p = p+1 #contagem de palavras, para sempre avançar para a seguinte que pode ser abreviada;
    return nome

URL = f'https://viacep.com.br/ws/{cep}/json/'
dados = requests.get(URL).text #Aqui vamos requisitar os dados da API dos correios para que seja retornado as informações que queremos;
dadosdic = json.loads(dados) #Vamos transformar os dados que conseguimos em um dicionario, para que seja possivel uma manipulação mais fácil;

informacoes.append(abrevia(nome)) #Vamos inserir todos os dados que conseguimos numa lista e já formata-los para exibição;
informacoes.append(abrevia(dadosdic["logradouro"]) + ", " + numero_casa)
informacoes.append(abrevia(dadosdic["localidade"]) + '/' + dadosdic["uf"])
informacoes.append(dadosdic["cep"])

for dados in informacoes: #Vamos exibir os dados de acordo com a posição deles na lista, assim como requisitado;
    print(dados)