class ArquivoDAO:

	def __init__(self, arquivo):
		self.arquivo = arquivo
		self.verificaArquivo()

	def verificaArquivo(self):
		try:
			arquivo = open(self.arquivo, "r")
		except:
			arquivo = open(self.arquivo, "w+")
		finally:
			arquivo.close()

	def salvar(self, dados):
		try:
			arquivo = open(self.arquivo, "a")
			arquivo.write(str(dados))
			arquivo.close()
			return 1
		except:
			return 0