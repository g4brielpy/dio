'''
modulos contendo todos os métodos de operações:
    1) deposito; 
    2) saque; 
    3) extrato
'''

# variáveis
lista_de_depositos = list()
lista_de_saques = list()


def deposito(saldo_atual):
    print('DEPOSITO')

    valor_deposito = float(input('Digite o valor do deposito: '))
    # adicionar valor ao saldo, caso seja positivo.
    if valor_deposito > 0:
        saldo_atual = saldo_atual + valor_deposito
        # lista de extrato com todos os depositos
        lista_de_depositos.append(valor_deposito)
        print(f'R$ {valor_deposito:.2f} Adicionado ao saldo')
    else:
        print('Valor inválido')

    return saldo_atual


def saque(saldo_atual, quantidade_saque, LIMITE):
    print('SAQUE')

    # veficar se pode efetuar saque
    if quantidade_saque == 3:
        print('Limite de saques diário atingido.')
        return saldo_atual, quantidade_saque

    valor_saque = float(input('Digite o valor do saque (max: R$ 500,00): '))

    # verificando se o valor do saque é valido
    if (valor_saque <= saldo_atual) and (valor_saque <= LIMITE):
        saldo_atual -= valor_saque
        # lista de extrato com todos os saques
        lista_de_saques.append(valor_saque)
        quantidade_saque += 1
        print(f'R$ {valor_saque:.2f} sacados')

    else:
        print('Valor inválido')

    return saldo_atual, quantidade_saque
