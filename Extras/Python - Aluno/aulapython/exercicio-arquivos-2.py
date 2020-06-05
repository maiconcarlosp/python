

entrada = open("usuarios.txt", "r")

usuarios = entrada.readlines()

relatorio = []



for chave, usuario in enumerate(usuarios):

	usuario = usuario.split("\t")
	usuario.append(int(chave)+1)

	relatorio.append(usuario)


total = 0.0


relatorio2 = []

for usuario in relatorio:

	mb = float(usuario[1].replace("\n", "")) / (1024 * 1024)

	usuario.append(mb)
	relatorio2.append(usuario)

	total = total + mb



saida = open("relatorio.txt", "w")

saida.write("""Empresa Inc.\tUso do espaço em disco por usuário \n""")
saida.write("-"*50 + "\n")	
saida.write("""Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n""")

for r in relatorio2:

	saida.write(str(r[2]) + "\t" + str(r[0]) + "\t" + str(r[3]) + "\t" + str(r[3] / total) + "\n")


saida.write("""Espaço total ocupado: {}""".format(total))
saida.write("""Espaço médio ocupado: {}""".format(total/len(relatorio2)))

entrada.close()
saida.close()