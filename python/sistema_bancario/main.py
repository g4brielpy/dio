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
# constantes
LIMITE = int(500)
LIMITE_SAQUE = int(3)

while True:
    # Operações solicitadas para o sistema
    menu = str('''  
    Operações:

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair
            
        : ''')
    opcao = str(input(menu))

    match opcao:
        case '1':
            print(saldo)
            saldo = operacoes.deposito(saldo)

        case '4':
            break
        case _:
            print('Operação inválida, digite novamente!')