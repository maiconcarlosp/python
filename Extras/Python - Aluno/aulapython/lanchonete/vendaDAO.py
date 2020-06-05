
from datetime import datetime

class vendaDAO:


	def __init__(self):
		self.nome = "venda-" + str(datetime.now().date()) + ".txt"
		self.verificaArquivo()


	def verificaArquivo(self):
		try:
			arquivo = open(self.nome, "r")
		except:
			arquivo = open(self.nome, "w+")
		finally:
			arquivo.close()

	def salvar(self, venda):
		try:
			arquivo = open(self.nome, "a")
			arquivo.write(str(venda))
			arquivo.close()
			return 1
		except:
			return 0