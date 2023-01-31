import json, xmltodict, requests
#IMPORTANTE, É NECESSÁRIO INSTALAR A BIBLIOTECA "xmltodict" PARA QUE SEJA POSSIVEL EXECUTAR ESTE CODIGO!!!
URL = 'http://servicos.cptec.inpe.br/XML/cidade/7dias/235/previsao.xml' #URL da api que disponibiliza essas previsões em XML;
requisicao = requests.get(URL).text # Aqui podemos obter os dados que precisamos;
xml = xmltodict.parse(requisicao) # Aqui vamos converter de XML para o formato python;
convert_json = json.dumps(xml) # Agora vamos converter o que conseguimos, para o formato json;
dicionario = json.loads(convert_json) # Agora vamos converter os dados em um dicionario, para que possamos utilizar nos próximos passos;
previsoes = dicionario.get("cidade") #Nesses passos vamos filtar as informações que queremos;
previsoes2 = previsoes.get("previsao")

print(f"/{'-'*26}\\")
for dias in previsoes2: #Aqui vamos formatar a maneira que queremos exibir os dados que conseguimos obter;
     print(f'|{dias["dia"]:10} | {dias["tempo"]:3} | {dias["minima"]:2} | {dias["maxima"]:2}|')
print(f"\\{'-'*26}/")