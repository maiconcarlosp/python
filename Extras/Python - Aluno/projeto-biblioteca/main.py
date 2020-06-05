
import os
import re
from to.cliente import Cliente

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

try:
    arquivo = open(BASE_DIR + "bd/cliente.txt", "r")
except:
    arquivo = open("bd/cliente.txt", "w+")
finally:
    arquivo.close()

try:
    arquivo = open("bd/idcliente.txt", "r")
except:
    arquivo = open("bd/idcliente.txt", "w+")
finally:
    arquivo.close()


def limpaTela():
    try:
        os.system("clear")
    except:
        os.system("cls")

def cadastraCliente():
    limpaTela()    
    cpf = input("Digite o CPF: ")
    c = Cliente(cpf)
    c.buscar()
    if c.nome == "" and c.cpf != "":
        while 1:
            c.nome = input("Digite o nome: ")
            c.telefone = input("Digite o telefone: ")
            if (c.nome != "") and (c.telefone != "") and (re.search(r"\([0-9][0-9]\)[0-9]+\-[0-9]+$", c.telefone)):
                c.salvar()
                break
            else:
                limpaTela()
                print("Fez besteira queridão.")        
    limpaTela()
    print("Cliente cadastrdo com sucesso")

while 1:

    print("""
    1 - Cadastra Cliente
    2 - Cadastra Livro
    3 - Empréstimo
    4 - Devolução
    0 - Sair\n""")

    opt = input("Vai: ")

    if opt == "0":
        print("Até a próxima!")
        input()
        break
    elif opt == "1":
        cadastraCliente()
    elif opt == "2":
        cadastraLivro()
    elif opt == "3":
        emprestaLivro()
    elif opt == "4":
        devolveLivro()
    else:
        limpaTela()
        print("Pirou?")
        continue


def cadastraLivro():
    pass