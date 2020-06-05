clientes = {}

def cadastra(cpf){
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    clientes[cpf] = {"nome": nome, "telefone": telefone}
}

while 1:

    cpf = input("Digite o CPF: ")
    if cpf in clientes.keys():
        opt = input("Cliente já existe. Atualizar?(S/N): ")
        if opt == "S":
            cadastra(cpf)
        else:
            continue
    else:
        cadastra(cpf)


    sair = input("Cadastrar o próximo?(S/N): ")
    if sair == "N":
        break