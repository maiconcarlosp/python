from factory import FileFactory

class Cliente(FileFactory):

	def __init__(self, nome="", cpf="", dataNascimento="", endereco="", email=""):
		super().__init__("cliente")
		self.nome = nome
		self.cpf = cpf
		self.dataNascimento = dataNascimento
		self.endereco = endereco
		self.email = email

	def salvar(self):
		item = {"nome": self.nome,
				"cpf": self.cpf,
				"dataNascimento": self.dataNascimento,
				"endereco": self.endereco,
				"email": self.email}
		super().salvar(item)

	def buscar(self):
		r = super().buscar(self.cpf)
		if r == "":
			pass
		else:
			r = eval(r)
			self.nome = r["nome"]
			self.cpf = r["cpf"]
			self.dataNascimento = r["dataNascimento"]
			self.endereco = r["endereco"]
			self.email = r["email"]