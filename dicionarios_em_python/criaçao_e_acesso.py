"""
Um dicionario é um conjunto nao-ordenado de pares chave:valor, onde as chaves sao 
unicas em uma dada instancia do dicionario. Dicionarios sao delimitados por chaves {}
e contem uma lista de pares chave:valor separada por virgula
"""
pessoa = {"nome": "Aiko", "idade": 23}

pessoa_2 = dict(nome = "kamille", idade = "22")

pessoa["telefone"] = "984616423"

print (pessoa)

# As chaves no dicionario sao valores imutaveis, mas seus valores sao

#Acesso:

print (pessoa["nome"])

print (pessoa_2["nome"])

"""
Dicionarios aninhados

Dicionarios podem armazenar qualquer tipo de objeto python como valor, desde que a chave para
esse valor seja um objeto imutavel como (strings e numeros)
"""
contatos = {
    "aiko58912@gmail.com" : {"nome": "Aiko", "telefone": "99999999"},
    "mutantetrakor82@gmail.com" : {"nome": "kamille", "telefone" : "44444444"}
}

print (contatos["aiko58912@gmail.com"]["telefone"])

"""
A forma mais comum de iterar um dicionario é atraves do comando for
"""
for chave, valor in contatos.items():
    print (chave, valor)





