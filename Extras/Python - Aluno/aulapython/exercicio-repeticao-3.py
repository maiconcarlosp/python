
nome = input("Qual o nome do aluno? ")

alunos = []

while nome != "":

	#Lista de informações do meu aluno
	aluno = []

	#Armazenamento do nome do aluno
	aluno.append(nome)


	#Repetição do pedido de nota deste aluno
	cont = 0
	while cont < 3:
		nota = float(input("Digite a nota do aluno: "))
		aluno.append(nota)
		cont = cont + 1

	alunos.append(aluno)

	nome = input("Qual o nome do aluno? ")

#Contrução do relatório do aluno
if len(alunos) != 0:

	for aluno in alunos:

		print("O nome do aluno é {}".format(aluno[0]))
		print("A primeira nota é {}".format(aluno[1]))
		print("A segunda nota é {}".format(aluno[2]))
		print("A terceira nota é {}".format(aluno[3]))
		media = (float(aluno[1]) + float(aluno[2]) + float(aluno[3])) / 3
		print("A média do aluno é {}".format(media))

else:
	print("Nenhum relatório a ser gerado.")