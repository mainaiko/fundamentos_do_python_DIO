# union, uni 2 conjuntos

conjunto_a = {1,2}
conjunto_b = {1,3,4}

print (conjunto_a.union(conjunto_b))

#intersection, exibe os objetos que sao iguais nos 2 conjuntos

print (conjunto_a.intersection(conjunto_b))

# difference, todo objeto que esta somente em um conjunto

print (conjunto_a.difference(conjunto_b))

# symmetric_difference, todo objeto que nao se tocam

print (conjunto_a.symmetric_difference(conjunto_b))

# issubset, verifica se todos os elementos de um determinado conjunto pertencem a outro

print (conjunto_a.issubset(conjunto_b))

# issuperset, mesma coisa do issubset mas inverso

print (conjunto_a.issuperset(conjunto_b))

# isdisjoint, verifica se todos os elementos de um conjunto NAO pertencem a outro

print (conjunto_a.isdisjoint(conjunto_b))

# add, adiciona um objeto ao conjunto, mas se ele ja existir é ignorado

conjunto_a.add(5)
print (conjunto_a)

# clear, pega o conjunto e limpa ele

conjunto_a.clear()
print (conjunto_a)
conjunto_a = {1, 2, 5}

# copy, pega o conjunto e gera uma copia 

conjunto_a.copy()

# discard, retira um objeto especifico, mas se ele nao existir nao da erro

print (conjunto_a)
conjunto_a.discard(5)
print (conjunto_a)

# pop, remove objetos em ordem

conjunto_b.pop()
print (conjunto_b)

# remove, remove um objeto, mas se ele nao existir da um erro

# in, verifica se um objeto esta no conjunto