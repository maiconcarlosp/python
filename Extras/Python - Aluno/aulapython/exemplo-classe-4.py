class Pessoa:

	def __init__(self, nome, cpf, telefone):
		self.nome = nome
		self.cpf = cpf
		self.telefone = telefone

	def jacare(self):
		pass

class Funcionario(Pessoa):
	

	def __init__(self, cargo, nome, cpf, telefone):
		super(Funcionario, self).__init__(nome, cpf, telefone)
		
		self.cargo = cargo

	def jacare(self):
		print("Vendo jacaré")


class Cliente(Pessoa):

	def __init__(self, nome, cpf, telefone, renda):
		super(Cliente, self).__init__(nome, cpf, telefone)
		self.renda = renda

	def jacare(self):
		print("Compro jacaré")

	@staticmethod
	def verificaCadastro(cadastro, nome, cpf, telefone, renda):
		
		for c in cadastro:

			if c.telefone == self.telefone:
				return cadastro


		cliente = Cliente(nome, cpf, telefone, renda)
		return cadastro.append(cliente)


cliente = Cliente("eumesmo", 12, 14, 16)
cliente.jacare()

f = Funcionario("eumesmo", 12, 14, "cargo")
f.jacare()