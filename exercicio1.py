print('Bem vindo a Loja do Ricardo José Rufino Júnior')

# Capturando o valor do pedido
valorDoPedido = float(input("Entre com o valor do pedido: "))

# Capturando o valor da quantidade de parcelas
quantidaDeParcelas = int(input("Entre com a quantidade de parcelas: "))

# Declaração da variável juros
juros =0

# Lógica para o cálculo de juros, reatribuindo o valor para cada condição
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

# Valor total da parcela baseado nos juros
valorDaParcela = valorDoPedido * (1 + juros) / quantidaDeParcelas 

# Valor total parcelado 
valorTotalParcelado = float(valorDaParcela  * quantidaDeParcelas)

print(f'O valor das parcelas é de R$: {valorDaParcela:.2f}')
print(f'O valor total parcelado é de R$: {valorTotalParcelado:.2f}')