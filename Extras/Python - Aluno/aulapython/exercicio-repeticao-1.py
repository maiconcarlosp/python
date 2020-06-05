turmas = int(input("Qual a quantidade de turmas? "))

cont = 0
media = 0

while cont < turmas:
	alunos = int(input("Qual a quantidade de alunos desta turma? "))

	if alunos <= 40 and alunos > 0:
		media = media + alunos
		cont = cont + 1
	else:
		print("Total de alunos incorreto. Repita.")

media = media / turmas

print("A média de alunos por turma é {}".format(media))