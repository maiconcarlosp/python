salario = float(input())
erro = 0

if salario > 0 and salario <= 1280.00:
	percentual = 20
	

elif salario > 1280.00 and salario <= 1700.00:
	percentual = 15

elif salario > 1700.00 and salario <= 2500.00:
	percentual = 10

elif salario > 2500.00:
	percentual = 5

else:
	erro = 1
	print("Valor digitado incorreto.")

if erro == 0:
	aumento = salario * percentual / 100
	novosalario = salario + aumento

	print("O salário inicial é: %s" % salario)
	print("O percentual aplicado é de {}%".format(percentual))
	print("O aumento será: R${}".format(aumento))
	print("O novo salário será: R${}".format(novosalario))