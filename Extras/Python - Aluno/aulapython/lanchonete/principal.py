
from produto import Produto
from produto import Bebida
from produto import Pizza
from produto import PizzaInteira

from pessoa import Cliente
from pessoa import Funcionario

from venda import Venda

produtos = {}

produtos["100"] = Produto(cdProduto=100, nmProduto="Cachoro quente", vlProduto=1.2)
produtos["101"] = Produto(cdProduto=101, nmProduto="Bauru simples", vlProduto=1.3)
produtos["102"] = Produto(cdProduto=102, nmProduto="Bauru com ovo", vlProduto=1.5)
produtos["103"] = Produto(cdProduto=103, nmProduto="Hambúrguer", vlProduto=1.2)
produtos["104"] = Produto(cdProduto=104, nmProduto="Cheeseburger", vlProduto=1.3)
produtos["105"] = Produto(cdProduto=105, nmProduto="Refrigerante", vlProduto=1.0)

produtos["106"] = Bebida(cdProduto=106, nmProduto="Suco de Laranja", vlProduto=3.9, volume=1000)

produtos["107"] = Pizza(cdProduto=107, nmProduto="Pizza pedaço", vlProduto=2.0)
produtos["108"] = ""

funcionario = ""


while True:
	
	print("1 - Vender")
	print("2 - Abertura de caixa")
	print("3 - Fechamento de caixa")
	print("4 - Mostrar relatório")
	print("5 - Cadastrar Cliente")
	print("6 - Cadastrar Funcionario")
	print("0 - Sair")

	opt = input("Digite a opção desejada: ")

	### Inicio da Venda ###
	if opt == "1":
		if funcionario == "":
			print("Faça a abertura de caixa primeiro.\n")
			continue
		else:
			venda = Venda()
			while True:				
				item = input("Digite o código do item: ")
				if item == "0":
					print(venda.vendaTotal())
					venda.salvar()
					break
				else:
					qtd = input("Digite a quantidade: ")
					
					if item == "108":
						tamanho = input("Digite o tamanho da pizza: ")
						produtos["108"] = PizzaInteira(cdProduto=108, nmProduto="Pizza Inteira", tamanho=tamanho)

					try:
						venda.vendeProduto(produtos[item], qtd)
					except:
						print("Código de produto inválido. \n")
						continue


	### Fim da Venda ###

	### Inicio da Abertura do Caixa ###
	elif opt == "2":
		if funcionario == "":
			funcionario = input("Digite o nome do funcionario: ")
			print("Caixa aberto!\n")
			continue
		else:
			print("O caixa já está aberto.\n")
			continue
	### Fim da Abertura do Caixa ###

	elif opt == "3":
		pass
	elif opt == "4":
		pass
	elif opt == "5":
		print("=== Cadastro do cliente ===\n")
		nome = input("Nome: ")
		cpf = input("Cpf: ")
		dtNascimento = input("Data de nascimento: ")
		fone = input("Telefone: ")

		cliente = Cliente(nome, cpf, fone, dtNascimento)
		v = cliente.salvar()
		if v:
			print("Cliente salvo com sucesso.\n")
		else:
			print("Falha ao cadastrar cliente.\n")

	elif opt == "6":
		print("=== Cadastro de funcionario ===")
		nome = input("Nome: ")
		cpf = input("Cpf: ")
		dtNascimento = input("Data de nascimento: ")
		fone = input("Telefone: ")
		nrMatricula = input("Matrícula: ")

		funcionario = Funcionario(nome, cpf, nrMatricula, fone, dtNascimento)
		v = funcionario.salvar()

		if v:
			print("Funcionário cadastrado com sucesso.\n")
		else:
			print("Falha ao cadastrar funcionário.\n")


	elif opt == "0":
		break
	else:
		print("Opção inválida\n")
		continue