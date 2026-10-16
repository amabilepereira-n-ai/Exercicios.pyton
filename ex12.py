#Leia dois números: o dividendo e o divisor. Se o divisor for zero, mostre Erro: não existe divisão por zero. Caso contrário, mostre o resultado da divisão.

dividendo = float(input("Digite seu dividendo: "))
divisor = float(input("Digite seu divisor: "))

if divisor <= 0:
    print("não existe divisão por zero.")

else:
    print("O resultado da sua divisão é: ", dividendo / divisor)