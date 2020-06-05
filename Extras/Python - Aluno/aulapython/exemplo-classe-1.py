class Cliente:

	def __init__(self, nome, idade, genero, cpf):
		
		self.nome = nome
		self.idade = idade
		self.genero = genero
		self.cpf = cpf

	def verificaCPF(self):
		print(self.cpf)


abacate = Cliente("Fulano", "31", "Seilá", 15)

abacate.verificaCPF()

print(abacate.nome)