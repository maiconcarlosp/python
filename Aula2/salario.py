valorHora = float(input("Quanto você ganha por hora?: "))
horas = float(input("Quantas horas trabalhadas por mês?: "))
bruto = valorHora * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - (ir + inss + sindicato)
print("Salário Bruto: R${:.2f}".format(bruto))
print("IR (11%): R${:.2f}".format(ir))
print("INSS (8%): R${:.2f}".format(inss))
print("Sindicato (5%): R${:.2f}".format(sindicato))
print("Salário Líquido: R${:.2f}".format(liquido))
