# modulos contendo todos os métodos de operações: deposito; saque; extrato
lista_de_depositos = list()


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



def saque(saldo_atual):
    print('SAQUE')