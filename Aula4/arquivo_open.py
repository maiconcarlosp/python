ips = open('Aula4/ips.txt', 'r')
linhas = ips.readlines()
ips.close()

invalidos = []
validos = []

for linha in linhas:
     validador = 1
     linha = linha.split('.')
          
     if int(linha[0]) == 0 or int(linha[0]) > 255: 
          invalidos.append('.'.join(linha))
          validador = 0
          continue
     
     for l in linha:
          if int(l) > 255:
               invalidos.append('.'.join(linha))
               validador = 0
               break

     if validador:
          validos.append('.'.join(linha))

saida = open('Aula4/ips_resultado.txt', 'w')

saida.write('IPs válidos:\n')
for valido in validos:
     saida.write(valido)

saida.write('IPs inválidos:\n')
for invalido in invalidos:
     saida.write(invalido)

saida.close