'''
Sistema bancario em python
Operações:
    . saque
    . depósito
    . extrato

Otimização:
    . Criar usuário
        O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. 
        O endereço é uma string com o formato: logradouro, nro bairro cidade/sigla estado. (não e obrigatório validar formato)
        Deve ser armazenado somente os números do CPF(Sem '.', '-'). 
        Não podemos cadastrar 2 usuários com o mesmo CPF.

    . Cria conta corrente
        O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. 
        O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". 
        O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
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
            saldo = operacoes.deposito(saldo_atual=saldo)
        case '2':
            saldo, quantidade_saque = operacoes.saque(
                saldo_atual=saldo, quantidade_saque=quantidade_saque, LIMITE=LIMITE)
        case '3':
            operacoes.extrato()
        case '4':
            break
        case _:
            print('Operação inválida, digite novamente!')
