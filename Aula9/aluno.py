class Aluno:

     def __init__(self, nome, notaUm, notaDois, notaTres):
          self.nome = nome
          self.notaUm = notaUm
          self.notaDois = notaDois
          self.notaTres = notaTres

     def media(self):
          return (int(self.notaUm) + int(self.notaDois) + int(self.notaTres)) / 3