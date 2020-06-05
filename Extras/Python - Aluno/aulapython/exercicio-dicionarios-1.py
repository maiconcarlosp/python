
import os
import statistics

base_dir = os.path.dirname( os.path.abspath(__file__) )

alunos = {}
matricula = 0

while 1:

	nome = input("Digite o nome do aluno: ")

	if nome == "":
		break

	#aluno = {"nome": nome}
	aluno = {}
	aluno["nome"] = nome

	notas = []

	for i in range(3):
		nota = input("Digite a nota {}: ".format(i+1))
		notas.append(int(nota))
	
	aluno["notas"] = notas

	matricula += 1
	alunos[matricula] = aluno


relatorio = os.path.join(base_dir, "relatorios")

if len(alunos):

	for matricula in alunos:
		aluno = alunos[matricula]
		arquivo = str(matricula) + "-" + aluno["nome"].replace(" ", "-") + ".txt"
		boletim = open( os.path.join(relatorio, arquivo), "w")

		boletim.write("Nome: {}\n".format(aluno["nome"]))
		for key, nota in enumerate(aluno["notas"]):
			boletim.write("Nota {}: {}\n".format(key+1, nota))

		boletim.write("Média: {}\n".format( statistics.mean(aluno["notas"]) ))

		boletim.close()