while 1:
     valor = input('Digite um valor: ')
     try:
          divisao = 1 / float(valor)
          print('A divisão é {:.2f}.'.format(divisao))
          break
     except ValueError:
          print('Precisa ser inserido um número válido!')
     except ZeroDivisionError:
          print('O resultado para essa divisão é infinito!')
          break
     except:
          print('Erro desconhecido, tente novamente!')
