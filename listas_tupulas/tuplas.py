"""
Tuplas em python

Tuplas sao estruturas de dados muito parecidas com as listas, a principal
diferença é que tuplas sao imutaveis enquanto listas sao mutaveis.

Podemos criar tuplas atravez da classe tuple, ou colocando valores separados 
por virgula
"""

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

print (numeros[0])
print (frutas[1])

"""
Matriz em tupla é muito parecido como nas listas
interessante para ser usado quando eu quero que o valor seja imutavel
"""

matriz = (
    ("aiko", "leticia", "vanessa"),
    (1,2,3,4)
)

print (matriz[0][1])
print (matriz[1][2])

"""
Fatiamento é igual a listas.
"""