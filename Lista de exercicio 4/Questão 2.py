#Codigo para identificar posição de numeros

n = 0
lista_de_numeros = []
contagem0a25  = 0
contagem26a50 = 0
contagem51a75 = 0
contagem76a100 = 0
contagem_maior100 = 0

while n >= 0: #Aqui vamos capturar os numeros que vamos armazenar;
    n = int(input("Digite um numero ou digite -1 para parar: "))
    if n >= 0: #Caso o numero seja menor que 0, será descartado e assim o laço será interrompido;
        lista_de_numeros.append(n)

for a in lista_de_numeros: #Aqui vamos verificar a quais grupos os numeros pertencem;
    if a > 0 and a <= 25: #Verificando se o valor do numeros está entre o limiar estipulado, caso não, passa para a condição seguinte;
        contagem0a25 = contagem0a25+1
    elif a > 25 and a <= 50:
        contagem26a50 = contagem26a50+1
    elif a > 50 and a <= 75:
        contagem51a75 = contagem51a75+1
    elif a > 75 and a <= 100:
        contagem76a100 = contagem76a100+1
    else:
        contagem_maior100 = contagem_maior100+1

resultado1 = int((contagem0a25*100)/len(lista_de_numeros))#Nessa parte do codigo vamos verificar a porcentagem de presença entre os diferentes grupos na lista;
resultado2 = int((contagem26a50*100)/len(lista_de_numeros))
resultado3 = int((contagem51a75*100)/len(lista_de_numeros))
resultado4 = int((contagem76a100*100)/len(lista_de_numeros))
resultado5 = int((contagem_maior100*100)/len(lista_de_numeros))

resultado = "São {0}% no intervalo entre 0 e 25, {1}% no intervalo 26 e 50, {2}% no intervalo 51 e 75, {3}% no intervalo 75 e 100, e {4}% maiores que 100."
print(resultado.format(resultado1,resultado2,resultado3,resultado4,resultado5)) #Por ultimo vamos exibir os resultados que obtivemos.