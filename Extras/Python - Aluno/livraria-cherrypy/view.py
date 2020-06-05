import cherrypy

from cliente import Cliente

class Root:

	@cherrypy.expose
	def index(self):
		return """
			<hmtl>
				<head>
				</head>
				<body>
					<table>
						<form method="post" action="cliente">
							<tr>
								<td><label> Nome: </label></td>
								<td><input type="text" name="nome" /></td>
							</tr>
							<tr>
								<td><label> Cpf: </label></td>
								<td><input type="text" name="cpf" /></td>
							</tr>
							<tr>
								<td><label> Data de nascimento: </label></td>
								<td><input type="text" name="dataNascimento" /></td>
							</tr>
							<tr>
								<td><label> Endereço: </label></td>
								<td><input type="text" name="endereco" /></td>
							</tr>
							<tr>
								<td><label> Email: </label></td>
								<td><input type="email" name="email" /></td>
							</tr>
							<tr>
								<td><input type="submit" value="Salvar"></td>
							</tr>
						</form>
					</table>
				</body>
			</html>
		"""

	@cherrypy.expose
	def cliente(self, nome, cpf, dataNascimento, endereco, email):
		cliente = Cliente(nome, cpf, dataNascimento, endereco, email)
		try:
			cliente.salvar()
			return """
				<hmtl>
				<head>
				</head>
				<body>
					<h1>Cliente salvo com sucesso</h1>
				</body>
			</html>
			"""
		except:
			return """
				<hmtl>
				<head>
				</head>
				<body>
					<h1>Falha ao salvar cliente.</h1>
				</body>
			</html>
			"""

	@cherrypy.expose
	def busca(self):
		return """
			<hmtl>
				<head>
				</head>
				<body>
					<table>
						<form method="post" action="retorno">
							<tr>
								<td><label> Cpf: </label></td>
								<td><input type="text" name="cpf" /></td>
							</tr>
							<tr>
								<td><input type="submit" value="Buscar"></td>
							</tr>
						</form>
					</table>
				</body>
			</html>
		"""

	@cherrypy.expose
	def retorno(self, cpf):
		cliente = Cliente(cpf=cpf)
		cliente.buscar()
		if cliente.nome == "":
			return """
				<hmtl>
				<head>
				</head>
				<body>
					<h1>Cliente não encontrado</h1>
				</body>
			</html>
			"""
		else:
			return """
				<hmtl>
				<head>
				</head>
				<body>
					<h2>Informações do cliente</h2>
					<br />
					<table>
						<tr>
							<td>Nome:</td>
							<td>{}</td>
						<tr>
						<tr>
							<td>Cpf:</td>
							<td>{}</td>
						<tr>
						<tr>
							<td>Data de nascimento:</td>
							<td>{}</td>
						<tr>
						<tr>
							<td>Endereço:</td>
							<td>{}</td>
						<tr>
						<tr>
							<td>Email:</td>
							<td>{}</td>
						<tr>
					</table>
				</body>
			</html>
			""".format( cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.endereco, cliente.email )


cherrypy.quickstart(Root())