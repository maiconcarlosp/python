# controle = 1

# while controle:
#      usuario = input('Insira um nome de usuário: ')
#      senha = input('Insira uma nova senha: ')
#      if senha == usuario:
#           print('A senha não pode ser igual ao nome de usuário!')
#      else:
#           print('Usuário cadastrado com sucesso!')
#           controle = 0

# melhor porque se estiverem diferentes não precisa entrar no loop
usuario = input('Insira um nome de usuário: ')
senha = input('Insira uma nova senha: ')

while usuario == senha:
     print('A senha não pode ser igual ao nome de usuário!')
     usuario = input('Insira um nome de usuário: ')
     senha = input('Insira uma nova senha: ')

print('Usuário cadastrado com sucesso!')