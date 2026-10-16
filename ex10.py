#Leia duas notas de um aluno e calcule a média. Mostre a média e a mensagem Aprovado se ela for maior ou igual a 7.0, ou Reprovado caso contrário.

nota1 = float(input("digite sua primeira nota1: "))
nota2 = float(input("digite sua segunda nota2: "))

media = (nota1 + nota2)/2

if media >= 7.0:
 print("Aprovado")

else:
    print("Reprovado")