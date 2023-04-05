#Código para calcular indice de massa corporal;

peso = int(input("Insira seu peso: "))
altura = float(input("Insira a sua altura(use ponto): "))

#Agora vamos calcular o IMC;
imc = round(peso/altura**2,1)

if imc < 18.5 :
    print("Seu IMC é: ",imc)
    print("Abaixo do peso ideal!!!")
elif imc > 18.5 and imc < 24.9 :
    print("Seu IMC é: ",imc)
    print("Peso normal!")
elif imc > 25 and imc < 29.9 :
    print("Seu IMC é: ",imc)
    print("Acima do peso!!")
elif imc > 30 and imc < 34.9 :
    print("Seu IMC é: ",imc)
    print("Sobrepeso!!!")
elif imc > 35 and imc < 39.9 :
    print("Seu IMC é: ",imc)
    print("Obesidade!!!")
else :
    print("Seu IMC é: ",imc)
    print("Obesidade grave!!!!")