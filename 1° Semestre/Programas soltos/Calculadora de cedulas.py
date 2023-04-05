#Código para calcular quantidade de cedulas de um troco;

total = float(input("Insira o valor total a ser pago: "))
pago = float(input("Insira o valor pago: "))
troco = round(pago-total, 2)

if troco<0 : print("Pagamento insificiente")
else :
    if troco>0 :
        #Vamos calcular a quantidade de cédulas que serão devolvidas ao cliente;
        print("O seu troco é de R$", troco)

        cem = int(troco/100)
        if cem>=1 : print("São", cem,"cedulas de R$100")
        resto = troco-cem*100

        cinquenta = int(resto/50)
        if cinquenta>=1 : print("São", cinquenta,"cedulas de R$50")
        resto = resto-cinquenta*50

        vinte = int(resto/20)
        if vinte>=1 : print("São", vinte,"cedulas de R$20")
        resto = resto-vinte*20

        dez = int(resto/10)
        if dez>=1 : print("São", dez,"cedulas de R$10")
        resto = resto-dez*10

        cinco = int(resto/5)
        if cinco>=1 : print("São", cinco,"cedulas de R$5")
        resto = resto-cinco*5

        dois = int(resto/2)
        if dois>=1 : print("São", dois,"cedulas de R$2")
        resto = resto-dois*2

        um = int(resto/1)
        if um>=1 : print("São", um,"moedas de R$1")
        resto = resto-um*1

        cinquenta_cents = int(resto/0.5)
        if cinquenta_cents>=1 : print("São", cinquenta_cents,"moedas de R$0,50")
        resto = resto-cinquenta_cents*0.5

        vintecinco_cents = int(resto/0.25)
        if vintecinco_cents>=1 : print("São", vintecinco_cents,"moedas de R$0,25")
        resto = resto-vintecinco_cents*0.25

        dez_cents = int(resto/0.1)
        if dez_cents>=1 : print("São", dez_cents,"moedas de R$0,10")
        resto = resto-dez_cents*0.1

        cinco_cents = int(resto/0.05)
        if cinco_cents>=1 : print("São", cinco_cents,"moedas de R$0,05")
    else : print("Não há troco!!!")