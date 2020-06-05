class Usuario:

	def __init__(self, nome, espaco, cdUsuario):
		
		self.nome = nome
		self.espaco = espaco
		self.cdUsuario = cdUsuario


	def byteParaMega():
		return float(self.espaco) / (1024*1024)