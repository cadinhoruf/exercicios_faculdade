print('Bem vindo a Loja do Ricardo Rufino')
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidaDeParcelas = int(input("Entre com a quantidade de parcelas: "))
juros =0
if quantidaDeParcelas < 4:
  juros = 0
elif quantidaDeParcelas >= 4 and quantidaDeParcelas < 6:
  juros = 4/100
elif quantidaDeParcelas >= 6 and quantidaDeParcelas < 9:
  juros = 8/100
elif quantidaDeParcelas >= 9 and quantidaDeParcelas < 13:
  juros = 16/100
else:
  juros = 32/100

valorDaParcela = valorDoPedido * (1 + juros) / quantidaDeParcelas 
valorTotalParcelado = valorDaParcela  * quantidaDeParcelas
print(f'O valor das parcelas é de R$: {valorDaParcela:.2f}')
print(f'O valor total parcelado é de R$: {valorTotalParcelado}')