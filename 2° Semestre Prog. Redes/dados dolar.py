import requests
soma_compra = 0
count_compra = 0
soma_venda = 0
count_venda = 0
ano = input("Insira o ano que deseja consultar: ")

url  = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

dados = requests.get(url).json()
dados_selecionados = (dados['value'])

for v in dados_selecionados:
    soma_compra = soma_compra + v['cotacaoCompra']
    count_compra = count_compra + 1
    soma_venda = soma_venda + v['cotacaoVenda']
    count_venda = count_venda + 1

media_compra = round(soma_compra / count_compra,4)
media_venda = round(soma_venda / count_venda,4)
print(media_compra,"/",media_venda)

# Questão 01: Solicitar o ano e a média das cotações de compra e
#             e venda do ano informado e as maiores cotações de 
#             compra e venda de cada mês 