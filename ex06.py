#Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e o troco. Considere que o valor pago é sempre suficiente.

preco = float(input("Digite o preço do lanche: ")) 
quantidade = int(input("Digite a quantidade de lanches: "))

valorTotal = preco * quantidade # diz que o valor total e preco multiplicado pela quantidade

print(f"O valor a ser pago é de: {valorTotal}")

troco = float(input("Digite o valor recebido: "))

trocoCliente = troco - valorTotal # aqui diz que o troco do cliente e o troco menos o valor total

print(f"O valor total da compra ficou em: {valorTotal}") #resultado
print(f"O cliente pagou {troco} e o valor do troco é de: {trocoCliente}") #resultado