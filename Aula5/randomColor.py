import random

cor = lambda: """rgb({},{},{})""".format(random.randint(0,255),random.randint(0,255),random.randint(0,255),)

resultado = cor()
print(resultado)