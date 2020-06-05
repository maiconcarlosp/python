class Cliente:

    def __init__(self, cpf, nome="", telefone=""):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def salvar(self):
        arquivo = open("bd/cliente.txt", "a")
        indice = open("bd/idcliente.txt", "a")

        arquivo.write(self.cpf + "," + self.nome + "," + self.telefone + "\n")
        indice.write(self.cpf + ";")

    def buscar(self):
        if self.cpf != "":
            indice = open("bd/idcliente.txt", "r")
            i = indice.read()
            indice.close()

            if self.cpf in i:
                del i
                arquivo = open("bd/cliente.txt", "r")
                linhas = arquivo.readlines()
                arquivo.close()

                for linha in linhas:
                    if self.cpf in linha:
                        cliente = linha.split(",")
                        self.nome = cliente[1]
                        self.telefone = cliente[2]
                        del cliente
                        break
                del linhas