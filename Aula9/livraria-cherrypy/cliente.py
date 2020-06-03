from factory import FileFactory
from factory import ConnectionFactory
import sqlite3
import os

class Cliente(ConnectionFactory):

	def __init__(self, nome="", cpf="", dataNascimento="", endereco="", email=""):
		# super().__init__("cliente")
		super().__init__()
		self.nome = nome
		self.cpf = cpf
		self.dataNascimento = dataNascimento
		self.endereco = endereco
		self.email = email

	""" def salvar(self):
		item = {"nome": self.nome,
				"cpf": self.cpf,
				"dataNascimento": self.dataNascimento,
				"endereco": self.endereco,
				"email": self.email}
		super().salvar(item) """

	def salvar(self):
		conn = sqlite3.connect(os.path.join(self.caminho, self.bd))
		cursor = conn.cursor()
		cursor.execute("""
	INSERT INTO cliente (nome, cpf, dataNascimento, email, endereco)
	VALUES('{}','{}','{}','{}','{}')
	""".format(self.nome, self.cpf, self.dataNascimento, self.email, self.endereco))
	conn.commit()
	cursor.close()
	conn.close()

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
