from usuario import Usuario

entrada = open("usuarios.txt", "r")

usuarios = entrada.readlines()

tamanho = len(usuarios)
cont = 0

total = 0.0


while cont < tamanho:

	a = usuarios[cont]
	a = a.replace("\n", "").split("\t")

	objeto = Usuario(a[0], a[1], cont + 1)	

	usuarios.remove(usuarios[cont])
	usuarios.insert(cont, objeto)

	total = total + objeto.byteParaMega()
	cont = cont + 1

saida = open("relatorio.txt", "w")

saida.write("""Empresa Inc.\tUso do espaço em disco por usuário \n""")
saida.write("-"*50 + "\n")	
saida.write("""Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n""")


for r in usuarios:

	saida.write(str(r.cdUsuario) + "\t" + r.usuario + "\t" + str(r.byteParaMega()) + "\t" + r.retornaPorcent(total) + "\n")


saida.write("""Espaço total ocupado: {}""".format(total))
saida.write("""Espaço médio ocupado: {}""".format(total/len(usuarios)))

entrada.close()
saida.close()