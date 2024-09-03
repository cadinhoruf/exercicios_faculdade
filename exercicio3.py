print("Bem-vindos à Fábrica de Camisetas do Ricardo José Rufino Júnior")

def escolha_modelo():
    modelos = ('MCS', 'MLS', 'MCE', 'MLE')
    while True:
        print('Entre com o modelo desejado:')
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Estampada")
        print("MLE - Manga Longa Estampada")
        modelo = input('>> ')
        
        if modelo not in modelos:
            print('Escolha inválida. Entre com o modelo novamente.')
            continue
        else:
            if modelo == "MCS":
                return 1.80
            if modelo == "MLS":
                return 2.10
            if modelo == "MCE":
                return 2.90
            if modelo == "MLE":
                return 3.20

def num_camisetas(valor):
    while True:
        try:
            numero_camisetas = int(input('Entre com o número de camisetas: '))
            
            if numero_camisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez. Por favor, entre com um número válido.')
                continue
            elif numero_camisetas < 20:
                desconto = 'Sem desconto'
                desconto_percentual = 0
            elif 20 <= numero_camisetas < 200:
                desconto = 'Desconto de 5%'
                desconto_percentual = 0.05
            elif 200 <= numero_camisetas < 2000:
                desconto = 'Desconto de 7%'
                desconto_percentual = 0.07
            elif 2000 <= numero_camisetas <= 20000:
                desconto = 'Desconto de 12%'
                desconto_percentual = 0.12
            
            valor_total = valor * numero_camisetas * (1 - desconto_percentual)
            
            return valor_total, desconto, numero_camisetas
        
        except ValueError:
            print('Número inválido. Entre com um número válido.')

def frete():
    while True:
        print('Escolha o tipo de frete:')
        print('1 - Frete por transportadora - R$ 100.00')
        print('2 - Frete por Sedex - R$ 200.00')
        print('0 - Retirar pedido na fábrica - R$ 0.00')

        opcoes = (0, 1, 2)
        frete_selecionado = input('>> ')
        try:
            frete_selecionado = int(frete_selecionado)
            if frete_selecionado == 0:
                return 0
            elif frete_selecionado == 1:
                return 100
            elif frete_selecionado == 2:
                return 200
            else:
                print('Opção inválida. Escolha novamente.')
                continue
        except ValueError:
            print('Entrada inválida. Digite um número.')
            continue

# Obtém o valor do modelo escolhido
valor_modelo = escolha_modelo()
# Obtém o valor total das camisetas com desconto aplicado, o tipo de desconto e a quantidade de camisetas
valor_total, desconto, quantidade_camisetas = num_camisetas(valor_modelo)
# Obtém o valor do frete selecionado
valor_frete = frete()

# Calcula o total final
total = valor_total + valor_frete

# Exibe o total final, a quantidade de camisetas, o tipo de desconto e o valor do frete
print(f'Total: R$ {total:.2f} (Modelo: R$ {valor_modelo:.2f} * Quantidade ({desconto}): {quantidade_camisetas} + frete: R$ {valor_frete:.2f})')
