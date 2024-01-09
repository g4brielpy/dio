'''
Sistema bancario em python
Operações:
    . saque
    . depósito
    . extrato
'''

# variáveis
saldo = float(0)

# Operações solicitadas para o sistema
menu = str('''  
Operações:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
           
    : ''')
opcao = str(input(menu))

