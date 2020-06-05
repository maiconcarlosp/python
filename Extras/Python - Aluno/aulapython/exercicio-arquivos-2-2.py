
import os

local = os.path.dirname( os.path.abspath(__file__) )
os.chdir(local)

ambiente = os.listdir()

u = 1
r = 1

for arquivo in ambiente:

	if arquivo == "usuario":
		u = 0

	if arquivo == "relatorio":
		r = 0

if u:
	os.mkdir("usuario")
if r:
	os.mkdir("relatorio")


for root, dirs, files in os.walk("usuario"):

	for f in files:
		print(f)

entrada = open("usuarios.txt", "r")

usuarios = entrada.readlines()

tamanho = len(usuarios)
cont = 0

total = 0.0

while cont < tamanho:


	usuario = usuarios[cont]

	usuario = usuario.replace("\n", "").split("\t")

	mb = float(usuario.pop()) / (1024 * 1024)

	usuario.append(mb)
	usuario.insert(0, cont + 1)


	usuarios.remove(usuarios[cont])
	usuarios.insert(cont, usuario)

	
	total = total + mb
	cont = cont + 1

saida = open("relatorio.txt", "w")

saida.write("""Empresa Inc.\tUso do espaço em disco por usuário \n""")
saida.write("-"*50 + "\n")	
saida.write("""Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n""")

for r in usuarios:

	saida.write(str(r[0]) + "\t" + str(r[1]) + "\t" + str(round(r[2], 2)) + "\t" + str(round((r[2] / total)*100, 2)) + "%\n")


saida.write("""Espaço total ocupado: {}""".format(total))
saida.write("""Espaço médio ocupado: {}""".format(total/len(usuarios)))

entrada.close()
saida.close()