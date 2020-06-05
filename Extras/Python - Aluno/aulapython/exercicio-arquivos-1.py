

entrada = open("ips.txt", "r")
ips = entrada.readlines()

valido = []
invalido = []

for ip in ips:

	ip = ip.replace("\n", "")

	octetos = ip.split(".")

	erro = 0

	if int(octetos[0]) == 0:
		invalido.append(ip)
		erro = 1
		continue
	else:
		for octeto in octetos:
			if int(octeto) > 255:
				invalido.append(ip)
				erro = 1
				break

	if erro == 0:
		valido.append(ip)

entrada.close()

saida = open("saida.txt", "w")

saida.write("IPs válidos \n")

for v in valido:
	saida.write(v + "\n")

saida.write("IPs invalidos \n")

for v in invalido:
	saida.write(v + "\n")

saida.close()