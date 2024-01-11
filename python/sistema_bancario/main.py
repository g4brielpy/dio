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
import user

# variáveis
saldo = float(0)
quantidade_saque = int(0)
usuarios = list()

# constantes
LIMITE = int(500)
LIMITE_SAQUE = int(3)

while True:
    # Operações solicitadas para o sistema
    menu = str(f'''
    OPERAÇÕES:
        [0] - Criar Usuário
        [1] - Cria Conta
        [2] - Depositar
        [3] - Sacar
        [4] - Extrato
        [5] - Sair

        SALDO DÍSPONIVEL: {saldo:.2f}
        SAQUES EFETUADOS: {quantidade_saque}

        : ''')
    opcao = str(input(menu))

    match opcao:
        case '0':
            usuarios = user.criar_usuario(usuarios)
            print(usuarios)
        case '2':
            saldo = operacoes.deposito(saldo_atual=saldo)
        case '3':
            saldo, quantidade_saque = operacoes.saque(
                saldo_atual=saldo, quantidade_saque=quantidade_saque, LIMITE=LIMITE)
        case '4':
            operacoes.extrato()
        case '5':
            break
        case _:
            print('Operação inválida, digite novamente!')
