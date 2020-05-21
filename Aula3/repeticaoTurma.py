turmas = int(input("Informe a quantidade de turmas: "))
if turmas > 0:
     count = 1
     alunos = 0
     while turmas >= count:
          alunos += int(input('Informe a quantidade de alunos na turma {}: '.format(count)))
          count += 1
     print('O total de alunos é {}'.format(alunos))
     print('A média de alunos por turma é {:.0f}'.format(alunos/turmas))
else:
     print('A turma deve ser um valor positivo ou diferente de 0')