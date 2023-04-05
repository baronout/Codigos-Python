def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def quant_primos(n):
    count = 0
    num = 2
    while count < n:
        if eh_primo(num):
            print(num)
            count += 1
        num += 1

n = int(input("Insira quantos numeros primos deseja imprimir: "))
quant_primos(n)
