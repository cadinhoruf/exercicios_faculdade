print('----- Bem-vindo à loja de marmitas do Ricardo José Rufino Júnior -----')
print('---------------------------- Cardápio --------------------------------')
print('--------| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) | -------')
print('--------|    P    |      R$ 16.00      |       R$ 15.00      | -------')
print('--------|    M    |      R$ 18.00      |       R$ 17.00      | -------')
print('--------|    G    |      R$ 22.00      |       R$ 21.00      | -------')
print('----------------------------------------------------------------------')

# Declara a variável acumuladora 
total = 0

# Inicia o loop while, com a condição True pois não há uma condição inicial para o loop, só para que ocorra
while True:
    # Recebe o valor do sabor
    sabor = input('Entre com o sabor desejado (BA/FF): ')
    sabores_aceitos = ('BA', 'FF')

    # Valida se o sabor escolhido está entre os sabores aceitos, se não retorna a pergunta
    if sabor not in sabores_aceitos:
        print('Sabor inválido. Tente novamente')
        continue

    # Recebe o valor do tamanho da marmita
    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    tamanhos_aceitos = ('P', 'M', 'G')

    # Valida se o tamanho está entre os tamanhos aceitos, se não retorna a pergunta
    if tamanho not in tamanhos_aceitos:
        print('Tamanho inválido. Tente novamente')
        continue
    # Condição aninhada para validar o sabor e tamanho da marmita
    if sabor == 'BA':
        if tamanho == 'P':
            valor = 16
        elif tamanho == 'M':
            valor = 18
        elif tamanho == 'G':
            valor = 22
    elif sabor == 'FF':
        if tamanho == 'P':
            valor = 15
        elif tamanho == 'M':
            valor = 17
        elif tamanho == 'G':
            valor = 21

    # Ternário para exibir o nome completo da marmita  
    nome_extenso = 'Bife Acebolado' if sabor == 'BA' else 'Filé de Frango'
    print(f'Você pediu um {nome_extenso} no tamanho {tamanho}: R${valor:.2f}')

    # Incrementa o valor ao total
    total += valor
    resposta = input('Deseja mais alguma coisa? (S/N): ')

    # Valida se quer fazer mais algum pedido, se não pausa o loop
    if resposta != 'S':
        break
# Exibe o valor total baseado na variável total 
print(f'O valor total a ser pago: R${total:.2f}')
