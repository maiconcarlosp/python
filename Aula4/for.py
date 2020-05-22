nomes = ['Maicon', 'Sabrina', 'Alexandre']
add = int(input('Quantos nomes gostaria de adicionar? '))
while add > 0:
     nomes.append(input('Faltam {} nomes, adicione: '.format(add)))
     add -= 1
     
for nome in nomes:
     print(nome)