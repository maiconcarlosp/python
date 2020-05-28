class Usuario:

    def __init__(self, nome, espaco, cdUsuario = ''):
          self.nome = nome
          self.cdUsuario = cdUsuario
          self.espaco = espaco

     def espacoMb(self):
          return (self.espaco / 1024) / 1024

     def percentualOcupado(self, total):
          """O total deve ser informado em Mb"""
          return (self.espacoMb / total) * 100
