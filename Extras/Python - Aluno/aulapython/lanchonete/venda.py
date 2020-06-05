from vendaDAO import vendaDAO

class Venda(vendaDAO):	

	def __init__(self):
		super().__init__()
		self.venda = {}

	def vendeProduto(self, produto, qtdProduto):
		
		if produto.cdProduto in self.venda.keys():
			#self.venda[produto.cdProduto] = self.venda[produto.cdProduto] + ( produto.vlProduto * int(qtdProduto) )
			self.venda[produto.cdProduto] += ( produto.vlProduto * int(qtdProduto) )
		else:
			self.venda[produto.cdProduto] = ( produto.vlProduto * int(qtdProduto) )
	

	def vendaTotal(self):

		total = 0

		for v in self.venda:
			total += self.venda[v]
		return total


	def salvar(self):
		#vDAO = vendaDAO()
		#v = vDAO.salvar(self.venda)
		v = super().salvar(self.venda)
		if v:
			return 1
		else:
			return 0