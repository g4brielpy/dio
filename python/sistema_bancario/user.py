'''
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

lista = list()


def criar_usuario(lista_de_usuarios):
    nome_input = str(input('Digite seu nome: '))
    data_nascimento_input = str(input('Digite sua data de nascimento: '))
    cpf_input = str(input('Digite seu CPF (somente número): '))
    endereco_input = str(input('Digite seu endereço: '))

    user = {
        'nome': nome_input,
        'nascimento': data_nascimento_input,
        'cpf': cpf_input,
        'endereco': endereco_input,
        'contas': ''
    }
    lista_de_usuarios.append(user)
    
    return lista_de_usuarios
