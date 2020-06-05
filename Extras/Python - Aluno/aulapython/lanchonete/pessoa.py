from arquivoDAO import ArquivoDAO

class Pessoa:

	def __init__(self, nome, cpf, fone, dataDeNascimento=""):
		self.nome = nome
		self.cpf = cpf
		self.fone = fone
		self.dataDeNascimento = dataDeNascimento

class Funcionario(Pessoa, ArquivoDAO):

	def __init__(self, nome, cpf, matricula, fone, dataDeNascimento):
		Pessoa.__init__(self, nome, cpf, fone, dataDeNascimento)
		ArquivoDAO.__init__(self, "funcionario.txt")
		self.matricula = matricula

	def salvar(self):
		dados = """{"nome":"%s", "cpf":"%s", "matricula":"%s", "fone":"%s", "dtNascimento":"%s"  }""" % (self.nome, self.cpf, self.matricula, self.fone, self.dataDeNascimento)
		v = ArquivoDAO.salvar(self, dados)
		if v:
			return 1
		else:
			return 0

class Cliente(Pessoa, ArquivoDAO):

	def __init__(self, nome, cpf, fone, dataDeNascimento):
		Pessoa.__init__(self, nome, cpf, fone, dataDeNascimento)
		ArquivoDAO.__init__(self, "cliente.txt")

	def salvar(self):
		dados = """{"nome":"%s", "cpf":"%s", "fone":"%s", "dtNascimento":"%s"  }""" % (self.nome, self.cpf, self.fone, self.dataDeNascimento)
		v = ArquivoDAO.salvar(self,  dados)
		if v:
			return 1
		else:
			return 0