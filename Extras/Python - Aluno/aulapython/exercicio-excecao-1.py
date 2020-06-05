
while 1:

	numero = input("Digite um inteiro: ")

	try:
		print( 1 / int(numero) )
		break
	except ZeroDivisionError:
		print("Infinito")
		break
	except ValueError:
		print("O valor digitado não é inteiro. Repita. \n")
	except:
		print("Erro desconhecido. Repita. \n")