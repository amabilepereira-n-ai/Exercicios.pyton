#Uma loja dá 10% de desconto em compras a partir de R$ 100,00. Leia o valor da compra e mostre o valor final a pagar.

compra = float(input("Digite o valor da sua compra: "))
 
if compra >= 100.00:
   desconto =  compra * 0.9
   print("O valor da sua compra é: ", desconto)

else: 
    print("O valor da sua compra é: ")