from factory import FileFactory

class Produto(FileFactory):

	def __init__(self):
		super().__init__("produto")