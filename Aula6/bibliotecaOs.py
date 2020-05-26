import os

# mostra a pasta atual
ambiente = os.getcwd()
print(ambiente)

# mostra o que existe dentro da pasta
ambiente = os.listdir()
print(ambiente)

# separa por tipo
inicio = os.getcwd()
for root, dirs, files in os.walk(inicio):
     print('Root: '+str(root))
     print('Diretórios: '+str(dirs))
     print('Arquivos: '+str(files))
     print('-'*50)

# entra na pasta
os.chdir('Aula5')

# criar diretorios
os.makedirs('bin/arquivos')

# remove diretorios somente se vazio, senão da exceção
os.rmdir('diretorio')

# remove árvore de diretórios desde que vazios
os.removedirs('bin/arquivos')

# nome do arquivo
base = os.path.basename(__file__)
print(base)

# diretório onde está instalado
base = os.path.dirname(__file__)
print(base)

# diretório absoluto desde a raíz de onde está instalado
base = os.path.abspath(__file__)
print(base)