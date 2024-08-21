#clear, limpa os dados do dicionario
pessoa = {"nome": "Aiko", "idade": 23}
pessoa.clear()

print (pessoa)

#copy, copia os objetos de um dicionario

pessoa = {"nome": "Aiko", "idade": 23}

pessoa_2 = pessoa.copy()

pessoa_2["nome"] = "Fatima"

print (pessoa)
print (pessoa_2)

# fromkeys, adiciona chaves de uma vez so

teste = pessoa.fromkeys(["telefone"], "vazio")
print (teste)

# get, acessa valores dentro de um dicionario, mas se ele nao existe ele retorna none

teste_2 = pessoa.get("chave", {})
print (teste_2)

# items, retorna uma lista de tupulas

teste_3 = pessoa.items()
print (teste_3)

# keys, retorna so as chaves do dicionario

print (pessoa_2.keys())

# pop, remove uma chave do dicionario, e retorna seu valor

print (pessoa.pop("nome"))
print (pessoa)

# popitem, remove uma chave do dicionario em ordem, nao precisa especificar qual chave

pessoa.popitem()
print (pessoa)

# setdefault, se a chave nao estiver no dicionario ele adiciona, mas se nao estiver retorna o valor que esta
#no dicionario.

pessoa = {"nome": "Aiko", "idade": 23}
print (pessoa.setdefault("nome", "jose"))

# update, permite atualizar um dicionario com outro dicionario

pessoa.update({"teste": {"telefone": "9999"}})
print (pessoa)
pessoa.update({"nome": "jose"})
print (pessoa)

# values, retorna somente os valores do dicionario

print (pessoa.values())

# in, verifica se ah uma chave no dicionario

print ("nome" in pessoa)

# del, remove itens especificos

del pessoa["nome"]
print (pessoa)


