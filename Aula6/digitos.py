frase = 'Houveram 12345 visitantes ontem.'

# somente números
digitos = [f for f in frase if f.isdigit()]

# somente letras
# digitos = [f for f in frase if f.isalpha()]

print(digitos)