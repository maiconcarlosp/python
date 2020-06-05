
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

soma = lambda x, y, z: x + y + z

total = soma(a, b, c)
print(total)