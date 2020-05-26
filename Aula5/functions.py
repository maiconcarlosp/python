def soma(a,b):
     return a + b

def subt(a,b):
     return a - b

def multi(a,b):
     return a * b

def divi(a,b):
     return a / b

a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
tipo = int(input('\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha o tipo de operação: '))

if tipo == 1:
     resultado = soma(a,b)
elif tipo == 2:
     resultado = subt(a,b)
elif tipo == 3:
     resultado = multi(a,b)
elif tipo == 4:
     resultado = divi(a,b)

print('Resultado: {}'.format(resultado))
