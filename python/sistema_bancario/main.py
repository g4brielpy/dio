'''
Sistema bancario em python
Operações:
    . saque
    . depósito
    . extrato
'''

import operacoes

# variáveis
saldo = float(0)
quantidade_saque = int(0)
# constantes
LIMITE = int(500)
LIMITE_SAQUE = int(3)

while True:
    # Operações solicitadas para o sistema
    menu = str(f'''
    OPERAÇÕES:

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair
               
        SALDO DÍSPONIVEL: {saldo:.2f}
        SAQUES EFETUADOS: {quantidade_saque}

        : ''')
    opcao = str(input(menu))

    match opcao:
        case '1':
            saldo = operacoes.deposito(saldo)
        case '2':
            saldo, quantidade_saque = operacoes.saque(saldo, quantidade_saque, LIMITE)

        case '4':
            break
        case _:
            print('Operação inválida, digite novamente!')
