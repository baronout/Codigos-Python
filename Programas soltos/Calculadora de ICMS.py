#Código para calcular ICMS 

valor_prod = float(input("Insira o valor do produto: "))
valor_venda = float(input("Insira o valor de venda do produto: "))

#Vamos calcular o ICMS tanto da compra quanto da venda;
icms_prod = float(valor_prod*0.17)
icms_venda = float(valor_venda*0.17)

#Agora vamos subtrair o icms da venda com o ICMS da compra para achar o ICMS  pago pela empresa;
icms_final = round(float(icms_venda-icms_prod),2)

print("O Valor pago pela empresa de ICMS é: R$", icms_final)