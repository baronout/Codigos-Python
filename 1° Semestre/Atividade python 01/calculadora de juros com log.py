import math
#Inserir os valores necessários para o calculo;
capital = float(input("Insira o valor a ser investido (use pontos ao invés da virgula para centavos): "))
montante = float(input("Insira o valor que quer chegar: "))
juros = float(input("Insira a taxa de juros mensal: "))
#Calculo do tempo necessário para chegar neste montante; 
t = int(math.log(montante/capital)/math.log(1+(juros/100)))
t = math.ceil(t)
print("O tempo para chegar neste valor é de ", t,"meses")