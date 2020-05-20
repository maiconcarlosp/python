# import statistics

# atribuir um alias
# import statistics as st

# ou
from statistics import mean

# opção 1
# nota1 = float(input("Insira a nota 1: "))
# nota2 = float(input("Insira a nota 2: "))
# nota3 = float(input("Insira a nota 3: "))
# nota4 = float(input("Insira a nota 4: "))
# print((nota1 + nota2 + nota3 + nota4) / 4)

# opção 2
notas = []
a = float(input('Digite a primeira nota: '))
notas.append(a)
a = float(input('Digite a segunda nota: '))
notas.append(a)
a = float(input('Digite a terceira nota: '))
notas.append(a)
a = float(input('Digite a quarta nota: '))
notas.append(a)


print(statistics.mean(notas))
# ou
# print(sum(notas)/len(notas))
# ou
# print((notas[0] + notas[1] + notas[2] + notas[3]) / 4)