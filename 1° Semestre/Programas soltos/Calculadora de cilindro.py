#Código para calcular volume do cilindro;
from cmath import pi


raio = float(input("Insira o raio do cilindro em cm: "))
altura = float(input("Insira a altura do cilindro em cm: "))

#Vamos calcular o volume agora;
volume = round(pi*raio**2*altura,2)
print("O volume do cilindro é:", volume,"cm³")