#codigo para contagem de numeros pares, impares e alguma operações

lista_de_numeros = []
numero = 1 #vamos começar com o valor 1 para que o laço possa iniciar, relaxe, pois ele logo é substituido pelo primeiro valor inserido pelo usuario;
numeros_par = 0
numeros_impar = 0
lista_par = []
lista_impar = []

while numero > 0: #aqui iniciamos um laço para decidir se os numeros devem ser aceitos na lista, case seja maior que 0, ele entra;
    numero = int(input("Insira um numero: "))
    if numero > 0:
        lista_de_numeros.append(numero)

for x in lista_de_numeros: #aqui vamos decidir se os numeros da lista são pares ou não, separando em quantidade e quem são eles;
    if x % 2 == 0:
        numeros_par = numeros_par+1
        lista_par.append(x)
    else:
        numeros_impar = numeros_impar+1
        lista_impar.append(x)

media_par = int((sum(lista_par))/len(lista_par)) #aqui vamos fazer a media deles, somando os numeros da lista e dividindo pela quantidade de termos da lista;
media_tudo = int((sum(lista_de_numeros))/len(lista_de_numeros)) #aqui vamos fazer a mesma operação anterior, mas não apenas com os pares;

resultados = "São {0} numeros pares e {1} numeros impares, a media dos pares é {2} e a media de todos os valores é {3}."
print(resultados.format(numeros_par,numeros_impar,media_par,media_tudo)) #aqui vamos formatar uma string para exibir os resultados obtidos;

if len(lista_de_numeros) >= 5: #Caso seja inserido 5 numeros ou mais, aparece essa mensagem especial;
    print("Feliz ano novo!!!!<(^_^)>)")