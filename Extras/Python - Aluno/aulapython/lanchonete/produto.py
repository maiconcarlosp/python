class Produto:

	def __init__(self, cdProduto, nmProduto = "", vlProduto = ""):
		self.cdProduto = cdProduto
		self.nmProduto = nmProduto
		self.vlProduto = vlProduto

	def __str__(self):
		return """{"cdProduto":"%s", "nmProduto":"%s", "vlProduto":"%s"}""" % (self.cdProduto, self.nmProduto, self.vlProduto)

class Bebida(Produto):

	def __init__(self, cdProduto,  volume, nmProduto = "", vlProduto = ""):
		super().__init__(cdProduto, nmProduto, vlProduto)
		self.volume = volume


class Pizza(Produto):

	def __init__(self, cdProduto, nmProduto = "", vlProduto = 2.0):
		super().__init__(cdProduto, nmProduto, vlProduto)

class PizzaInteira(Pizza):

	def __init__(self, cdProduto, tamanho, nmProduto = ""):
		super().__init__(cdProduto, nmProduto)
		self.tamanho = tamanho
		self.valorPizza()

	def valorPizza(self):

		if self.tamanho == "Brotinho":
			self.vlProduto = self.vlProduto * 4
		elif self.tamanho == "Grande":
			self.vlProduto = self.vlProduto * 8
		elif self.tamanho == "Gigante":
			self.vlProduto = self.vlProduto * 12