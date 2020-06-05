import cherrypy

from cliente import Cliente

class Root:


	@cherrypy.expose
	def index(self):
		return """
		<html>
	<head>
		<title>Meu sistema em CherryPy</title>
	</head>

	<body>

		<h1>Aplicação do professor</h1>

		<form method="post" action="verificaCliente">

			<label>Busca cliente por CPF:</label>
			<input type="text" name="clienteCpf" />

			<input type="submit" values="Verificar" />

		</form>


		<form method="post" action="verificaFuncionario">

			<input type="text" name="funcionarioCpf" />

			<input type="submit" values="Verificar" />

		</form>


	</body>


</html>
		"""


	@cherrypy.expose
	def verificaCliente(self, clienteCpf, nome = "", nascimento = "", renda = ""):

		if nome != "":
			c = Cliente(clienteCpf, nome, nascimento, renda)
			c.cadastraCliente()

		c = Cliente(clienteCpf)
		c.buscaCliente()

		if c.nome != "":
			return """
				CPF: {} <br />
				Nome: {} <br />
				Data de nascimento: {} <br />
				Renda: {} <br />
			""".format(c.cpf, c.nome, c.nascimento, c.renda)
		else:
			return """
			<html>
				<head>
					<title>Meu sistema em CherryPy</title>
				</head>
				<body>
					<form method="post" action="verificaCliente">
						<label>CPF:</label>
						<input type="text" name="clienteCpf" />
						<br />
						<label>Nome:</label>
						<input type="text" name="nome" />
						<br />
						<label>Data de nascimento:</label>
						<input type="text" name="nascimento" />
						<br />
						<label>Renda:</label>
						<input type="text" name="renda" />

						<input type="submit" values="Cadastrar" />

					</form>
				</body>
			</html>
			"""


	def cadastroCliente(self):
		pass

	