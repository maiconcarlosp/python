class Cliente:

     # método construtor, define os atributos que serão utilizados (passo somente uma vez no inicio do programa)
     def __init__(self, nome, telefone, dataNascimento, cpf = ''):
          self.nome = nome
          self.cpf = cpf
          self.telefone = telefone
          self. dataNascimento = dataNascimento

     # método destrutor, deleta os atributos
     def __del__(self):
          print('Objeto {} morreu'.format(self.nome))

     def verificaCpf(self):
          pass

c = Cliente('Abacate', 50, '01/01/1970', 12)
d = Cliente('Laranja', 52, '01/01/1980')
e = Cliente(cpf = 16, nome = 'Maçã', dataNascimento = '01/01/1990', telefone = 54)

# encerra o cliente c
del c

a = input('Pressione enter para matar os outros')
