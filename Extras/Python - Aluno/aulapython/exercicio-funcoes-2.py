
def valorPagamento(pago, atraso):

	if atraso <=0:
		return pago
	else:
		pago = pago + (pago * 0.03) + ((pago * 0.001)*atraso)
		return pago


dia = []

valor = float(input())
dias = int(input())

while valor != 0:

	resultado = valorPagamento(pago = valor, atraso = dias)
	print(resultado)
	dia.append(resultado)

	valor = float(input())
	dias = int(input())

for d in dia:
	print(str(d) + "\n")