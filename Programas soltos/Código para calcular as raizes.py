#Código para calcular as raizes das formula de bhaskara.
#30/10/2022

#O primeiro passo é inserir valores dos coeficientes A, B e C;

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

if a!=0 :

    #Como segundo passo, resolução do Delta da equação;
    d = b**2-4*a*c
    print("O valor para Delta é: ",d)
    if d>=0 :
        
        #Agora o próximo passo é calcular as raízes da equação;

        x1 = (-b+d*0.5)/(2*a)
        x2 = (-b-d*0.5)/(2*a)

        #Por último só precisamos exibir o resultado;

        print ("O valor de X1 é: ", x1)
        print ("O valor de X2 é: ", x2)
    else : print("A equação não possui raízes reais!!!")
else : print("Não é possível calcular as raízes com 'A' igual a 0!!!")