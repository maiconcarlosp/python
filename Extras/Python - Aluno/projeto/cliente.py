class Cliente:


	def __init__(self, cpf, nome = "", nascimento = "", renda = ""):
		self.cpf = cpf
		self.nome = nome
		self.nascimento = nascimento
		self.renda = renda

		try:
			arquivo = open("bd.cliente", "r")
		except:
			arquivo = open("bd.cliente", "a")
		finally:
			arquivo.close()

	def buscaClientes(self):

		try:
			arquivo = open("bd.cliente", "r")
			clientes = arquivo.readlines()
			arquivo.close()
		except:
			return list()

		lista = []

		for cliente in clientes:
			cliente = cliente.replace("\n", "").split(";")
			a = Cliente(cliente[0], cliente[1], cliente[2], cliente[3])
			lista.append(a)

		return lista

	def buscaCliente(self):

		try:
			arquivo = open("bd.cliente", "r")
			clientes = arquivo.readlines()
			arquivo.close()
		except:
			pass

		for cliente in clientes:
			cliente = cliente.replace("\n", "").split(";")
						
			if self.cpf == cliente[0]:
				self.nome = cliente[1]
				self.nascimento = cliente[2]
				self.renda = cliente[3]
				break

	def cadastraCliente(self):

		try:
			arquivo = open("bd.cliente", "a")
		except:
			return 1

		c = """{};{};{};{};\n""".format(self.cpf, self.nome, self.nascimento, self.renda)

		try:
			arquivo.write(c)
		except:
			return 1
		finally:
			arquivo.close()

		return 0