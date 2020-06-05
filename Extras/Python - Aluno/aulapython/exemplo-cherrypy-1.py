import cherrypy

class Root:

	@cherrypy.expose
	def index(self):

		return """
	<html>
		<head></head>

		<body>

			<form action="cliente" method="post">
				
				<label>Nome:</label>
				<input type="text" name="nome" />
				<br />
				<label>CPF:</label>
				<input type="text" name="cpf"/>
				<br />
				<label>Endereco:</label>
				<input type="text" name="endereco" />
				<br />
				<label>Idade:</label>
				<input type="text" name="idade" />
				<br />
				<input type="submit" value="Enviar" />

			</form>

		</body>

	</html>

		"""

	@cherrypy.expose
	def cliente(self, nome, cpf, endereco, idade):

		return """
		Nome: {} <br/>
		CPF: {} <br/>
		Endereço: {} <br/>
		Ano de nascimento: {}
		""".format(nome, cpf, endereco, 2019-int(idade))


cherrypy.quickstart( Root() )