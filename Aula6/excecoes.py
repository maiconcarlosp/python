# exemplo 1
try:
     arquivo = open('teste.txt', 'r')
     print('Arquivo aberto!')
except:
     arquivo = open('teste.txt', 'w+')
     print('Arquivo criado!')
else:
     texto = arquivo.readlines()
finally:
     arquivo.close()

# exemplo 2
# a = input('Digite um valor: ')
# try:
#      divisao = 1 / int(a)
# except ValueError:
#      print('Valor não pode ser convertido para inteiro!')
# except ZeroDivisionError:
#      print('Valor não pode ser zero!')
# except:
#      print('Erro desconhecido')
# finally:
#      print('Fim do programa.')