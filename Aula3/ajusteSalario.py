inicial = float(input("Quanto você ganha atualmente?: "))
if inicial >= 0:
     if inicial <= 1280:
          percentual = 20
     elif inicial > 1280 and inicial <= 1700:
          percentual = 15
     elif inicial > 1700 and inicial <= 2500:
          percentual = 10
     elif inicial > 2500:
          percentual = 5

     aumento = inicial * (percentual / 100)
     final = inicial + aumento

     print("Salário inicial: R${:.2f}".format(inicial))
     print("O percentual de aumento foi: {}%".format(percentual))
     print("O valor de aumento foi: R${:.2f}".format(aumento))
     print("Salário final: R${:.2f}".format(final))
     
else:
     print('Salário não pode ser negativo')