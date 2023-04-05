#Código para calcular salário de vendedor;
import math

salario = float(input("Insira o salario base do vendedor: "))
carro_vendi = int(input("Insira a quantidade de carros vendidos: "))
comissao_fixa = int(input("Insira a comissão por carro vendido: "))
valor_vendas = int(input("Insira o valor total das vendas: "))

salario_final = math.ceil(salario+(comissao_fixa*carro_vendi)+(valor_vendas*(6/100)))

print("O salario final do vendedor é: R$", salario_final)
