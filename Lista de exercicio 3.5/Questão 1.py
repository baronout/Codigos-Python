decrescente = True
digAnterior = 0
quant_decres = 0
for n in range(1,10001):
    digito = n % 10
    if digito < digAnterior:
        decrescente = False
    digAnterior = digito
    if decrescente == True:
        quant_decres = quant_decres+1
print(quant_decres)
