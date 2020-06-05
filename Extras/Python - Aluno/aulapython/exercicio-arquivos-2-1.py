
entrada = open("usuarios.txt", "r")

usuarios = entrada.readlines()

relatorio = []

total = 0.0

for chave, usuario in enumerate(usuarios):

	usuario = usuario.replace("\n", "").split("\t")

	mb = float(usuario.pop()) / (1024 * 1024)	

	total = total + mb

	usuario.append(mb)
	usuario.insert(0, int(chave) + 1)

	relatorio.append(usuario)



saida = open("relatorio.txt", "w")

saida.write("""Empresa Inc.\tUso do espaço em disco por usuário \n""")
saida.write("-"*50 + "\n")	
saida.write("""Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n""")

for r in relatorio:

	saida.write(str(r[0]) + "\t" + str(r[1]) + "\t" + str(round(r[2], 2)) + "\t" + str(round((r[2] / total)*100, 2)) + "%\n")


saida.write("""Espaço total ocupado: {}""".format(total))
saida.write("""Espaço médio ocupado: {}""".format(total/len(relatorio)))

entrada.close()
saida.close()