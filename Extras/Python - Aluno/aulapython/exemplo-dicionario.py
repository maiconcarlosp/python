#Declarar dicionario:

d = dict()
d = {}
d = {"cliente":"Alexandre", "seila":"Batman", "texto":12, "outra":True}

#d = dict(linha)

arvore = {"a": {
    "Alexandre": 12,
    "André": 14,
    },
    "b": {
        "Batman": 16,
        "Bruno": 18,
    }
}

cliente = {
    "12": {
        "nome": "Batman",
        "endereco": "Caverna",
        "telefone": [50, 51],
    },
    "14": {

    },
}


#Busca:

print(d["seila"])
print(arvore["b"]["Batman"])

print(cliente["12"])
print(cliente["12"]["telefone"][0])

print( len(cliente["12"]["telefone"]) )

#Adição
chave = input()
valor = input()
d["abacate"] = {chave:valor}

print("O"*100)
print(d)
print("O"*100)

cliente["12"]["telefone"].append("52")
cliente["12"]["Nome"] = "Seila"
#Métodos
print(d)

print("-"*50)
print( cliente["12"].keys() )

print( cliente["12"].values() )

if "12" in cliente.keys():
    print("seila")

# Caracteristicas

cliente["16"] = {} #Cria, pois não existe
cliente["14"] = {} #Substitui, pois já existe

print("\n" + "-"*50)

for c in cliente:
    print( c )
    
