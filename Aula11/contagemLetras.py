from collections import Counter

frase = input('Digite sua frase: ')

frase = frase.lower()
frase = frase.replace(" ", "")
frase = frase.replace("\n", "")
frase = frase.replace(".", "")
frase = frase.replace("!", "")
frase = frase.replace("?", "")
frase = frase.replace(",", "")
frase = frase.replace(";", "")

frase = frase.replace("á", "a")
frase = frase.replace("à", "a")
frase = frase.replace("ã", "a")
frase = frase.replace("é", "e")
frase = frase.replace("ê", "e")
frase = frase.replace("í", "i")
frase = frase.replace("ó", "o")
frase = frase.replace("ô", "o")
frase = frase.replace("ú", "u")
frase = frase.replace("ç", "c")

vogais = 0
consoantes = 0

for caracter in frase:
     if caracter in 'aeiou':
          vogais += 1
     else:
          consoantes += 1

print("Vogais: {}\nConsoantes: {}\nTotal de letras: {}".format(vogais, consoantes, len(frase)))

letras = Counter(frase)
quantidades = Counter(frase).values()

print('\nAs letras aparecem:')
for letra in letras:
     print('{} = {}'.format(letra, letras[letra]))