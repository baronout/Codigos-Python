import math
#Código para calcular raizes utilizando newton-raphson;

#Vamos declarar as variaveis e calcular os primeiros valores;
x0 = float(input("Digite a aproximação inicial x0: "))
iteracoes = int(input("Digite o numero máximo de iterações: "))
iteracao = 0
fx = pow(x0,2)-math.exp(x0)
f_linhax = 2*x0-math.exp(x0)

#Agora calcular a serie de valores solicitados de acordo com as iterações;
while iteracao <= iteracoes:
    x1 = x0-fx/f_linhax
    x0 = x1
    iteracao = iteracao+1
    print("A raiz encontrada foi x=", x1)





