"""
Criando sets
Um set é uma coleçao que nao possui objetos repetidos, usamos sets para
representar conjuntos matematicos ou eliminar itens duplicados de um iteravel
"""
# set remove itens duplicados

numeros = set([1,2,3,1,3,4])

print (numeros)

frutas = {"laranja", "pera", "maça", "laranja"}

print (frutas)


#mas ele nao garante a ordem
"""
Conjuntos em python nao suportam indexaçao e nem fatiamento, caso queira acessar
os seus valores é necessario converter o conjunto para lista
"""
frutas = list(frutas)
print(frutas[0])

"""
A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for
"""

mulheres = {"Aiko", "Fernanda", "Aiko"}

for woman in mulheres:
    print (woman)

"""
funçao enumerate
As vezes é necessario saber qual o indice do objeto dentro do laço for. Para isso podemos
usar a funçao enumerate
"""

for indice, woman in enumerate(mulheres):
    print (f"{indice}: {woman}")
    