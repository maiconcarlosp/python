import os
import sqlite3

class FileFactory:

	def __init__(self, arquivo):
		self.arquivo = arquivo
		self.caminho = os.path.dirname( os.path.abspath(__file__) )
		try:
			self.testeArquivo = open( os.path.join(self.caminho, arquivo), "r" )
		except:
			self.testeArquivo = open( os.path.join(self.caminho, arquivo), "w" )
		finally:
			self.testeArquivo.close()

	def salvar(self, item):
		saida = open( os.path.join(self.caminho, self.arquivo), "a" )
		saida.write( str(item) + "\n" )
		saida.close()

	def buscar(self, item):
		busca = open( os.path.join(self.caminho, self.arquivo), "r" )
		linhas = busca.readlines()
		busca.close()

		for linha in linhas:
			if item in linha:
				return linha
		return ""

class ConnectionFactory:

	def __init__(self):
		self.caminho = os.path.dirname(os.path.abspath(__file__))
		try:
			conn = sqlite3.connect(os.path.join(self.caminho, 'livraria.db'))
		except:
			print('Falha ao conectar no banco!')
		else:
			conn.close()

	def salvar(self):
		pass