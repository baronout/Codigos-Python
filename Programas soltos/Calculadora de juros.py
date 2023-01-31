#Código para calcular valorização de um valor sobre uma base de juros;

c = float(input("Insira o valor a ser investido (use pontos ao invés da virgula para centavos): "))
i = float(input("Insira a taxa de juros ao mês (use ponto ao invés da virgula): "))
t = int(input("Insira quantos meses você quer deixar o dinheiro render: "))

m = c*((1+(i/100))**t)
m = round(m, 2)
print("O valor investido somado ao juros acumulado é: ", m,"reais")