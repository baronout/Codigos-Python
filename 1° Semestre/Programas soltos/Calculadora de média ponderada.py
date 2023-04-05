#Código para calcular média ponderada;

trab1 = int(input("Insira a sua nota do primeiro trabalho: "))
prova1 = int(input("Insira a nota da sua primeira prova: "))
trab2 = int(input("Insira a nota do seu segundo trabalho: "))

#Vamos calcular as notas de cada bimestre;

#Vamos calcular a nota que falta para ser aprovado;
nota_falta = round(((6*(0.4+0.6))-(prova1*0.7)-(trab1*0.3)-(trab2*0.3))*-1, 2)

print("Você precisa de",nota_falta,"na próxima prova.")