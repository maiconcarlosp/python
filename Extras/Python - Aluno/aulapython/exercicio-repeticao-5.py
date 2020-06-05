while True:

	atd = input("Próximo cliente? (0 pra sair) ")

	if atd == "0":
		break
	else:
		total = 0
		qtdProduto = [0, 0, 0, 0, 0, 0]

		while True:
			produto = input("Digite o código do produto: ")
			qtd = input("Digite a qtd do produto: ")

			if produto == "0":

				print("Produto 100: %s" % qtdProduto * 1.2)
				print("Produto 101: %s" % qtdProduto * 1.3)
				print("Produto 102: %s" % qtdProduto * 1.5)
				print("Produto 103: %s" % qtdProduto * 1.2)
				print("Produto 104: %s" % qtdProduto * 1.3)
				print("Produto 105: %s" % qtdProduto * 1.0)
				print("O valor total foi: %s" % total)
				break
			elif produto == "100":
				qtdProduto[0] += int(qtd)
				produto = 1.2
			elif produto == "101":
				qtdProduto[1] += int(qtd)
				produto = 1.3
			elif produto == "102":
				qtdProduto[2] += int(qtd)
				produto = 1.5
			elif produto == "103":
				qtdProduto[3] += int(qtd)
				produto = 1.2
			elif produto == "104":
				qtdProduto[4] += int(qtd)
				produto = 1.3
			elif produto == "105":
				qtdProduto[5] += int(qtd)
				produto = 1.0

			total = total + (produto * int(qtd))