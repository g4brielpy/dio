'''
modulos contendo todos os métodos de operações:
    1) deposito;
        qualquer valor positivo

    2) saque; 
        3 saques
        R$ 500 maximo
        retorna 2 valores
            1. saldo
            2. quantidade de saque

    3) extrato
        Lista de saques
        Lista de depositos
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
    """
    Deve ser possível depositar valores positivos para a minha conta bancária. 
    A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
    Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
    """


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

    elif valor_saque > saldo_atual:
        print('Saldo não disponível')

    else:
        print('Valor inválido')

    return saldo_atual, quantidade_saque
    """
    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
    Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
    Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
    """


def extrato():
    print('EXTRATO')

    # verificar se houve alguma movimentação
    if (lista_de_depositos == []) and (lista_de_saques == []):
        print('Não foram realizadas movimentações')
        return

    # exibindo lista com valores
    if lista_de_saques:
        print(f'Lista de saques: R$ {lista_de_saques}')
    if lista_de_depositos:
        print(f'Lista de depositos: R$ {lista_de_depositos}')

    """
    Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
    Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

    Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
        1500,45 -- R$ 1500.45
    """
