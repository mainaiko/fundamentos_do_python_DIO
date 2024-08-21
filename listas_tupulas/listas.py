"""
Listas:
Estruturas amplamente utilizadas em todas as aplicaçoes python
Listas em python podem armazenar de maneira sequencial qualquer tipo de objeto.
Podemos criar listas utilizando o contrutor list, a funcao range ou colocando valores separados
por virgula dentro de [].
Listas sao objetos mutaveis portando podemos alterar seus valores apos a criaçao
"""
#Ex de listas:

frutas = ["laranja", "maca", "uva"]

letras = list("python")

numeros = list(range(10))

carro = ["ferrari", "F8", 4200000, 2020, 2900, "Brasilia", True]

"""
Acesso direto
A lista é uma sequencia, portando podemos acessar seus dados utilizando indices.
Contamos o indice de determinada sequencia a partir do zero
"""
print(letras[0])
print(frutas[-1])

"""
Listas aninhadas
Listas podem armazenar todos os tipos de objetos python, portando podemos ter listas que armazenam outras listas.
Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os indices de linha e coluna
"""

frutas = ["laranja", "maca", "uva", letras[0]]
print (frutas)
matriz = [
    [1,"a",2],
    [3,"b",4],
    [5,"c",6]
]
print(matriz[0][0])
print(matriz[1][-1])

"""
Fatiamento
Alem de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequencia.
Para isso basta passar o indice e/ou final para acessar o conjunto.
Podemos ainda informar qunantas posiçoes o cursos deve "pular" no acesso
"""
letras_2 = list("python")

print(letras_2[0:3])
print(letras_2[:3])
print(letras_2[:5:2])
print(letras_2[::-1])

"""
Compressao de listas
A compresao de listas oferece uma sintaxe mais curta quando voce deseja:criar uma nova lista com base nos valores
de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificaçao nos elementos de uma lista existente.
"""
#Filtro versao 1
numeros = list(range(20))
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares, "\n", impares)

#Filtro versao 2
par = [numero for numero in numeros if numero % 2 == 0]
print(pares)
impar = [numero for numero in numeros if numero % 2 != 0]
print(impar)