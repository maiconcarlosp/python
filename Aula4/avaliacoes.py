nome = input("Insira o nome do aluno? ")
alunos = []

while nome != "":
	aluno = []
	aluno.append(nome)
	cont = 0

	while cont < 3:
		nota = float(input("Digite a nota do aluno: "))
		aluno.append(nota)
		cont += 1

	alunos.append(aluno)
	nome = input("Insira o nome do aluno? ")

# Se for 0 é igual a false, o que não entra no if
if len(alunos):
	for aluno in alunos:
		print("O nome do aluno é {}".format(aluno[0]))
		print("A primeira nota é {}".format(aluno[1]))
		print("A segunda nota é {}".format(aluno[2]))
		print("A terceira nota é {}".format(aluno[3]))
		media = (float(aluno[1]) + float(aluno[2]) + float(aluno[3])) / 3
		print("A média do aluno é {}\n".format(media))
else:
	print("Nenhum relatório a ser gerado.")