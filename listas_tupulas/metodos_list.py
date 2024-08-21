#Metodos da classe list
''''''''''''''''''''''''
#Append, adiciona objetos a lista
lista = []

lista.append(1)
lista.append("Aiko")
lista.append([1,2,3,4])
print(lista)

#Clear, limpa os valores da lista
lista.clear()
print(lista)

#Copy, cria uma lista igual mas nao interfere na original
lista = [1, "Aiko", [1,2,3,4]]

lista_2 = lista.copy()
print(id(lista), id(lista_2))

#Count, usado para determinar quantas vezes um objeto aparece na lista
cores = ["preto", "roxo", "rosa", "rosa"]

print (cores.count("rosa"))

#Extend, adiciona novos elementos por meio de uma outra lista, nao vai eliminar os valores duplicados
linguagens = ["python", "javascript", "CSS"]
print(linguagens)

linguagens.extend(["python", "java", "cobol", "C++"])
print(linguagens)

#Index, retorna a primeira psiçao do objeto

linguagens = ["python", "js", "c", "java", "csharp"]

print (linguagens.index("js"))
print (linguagens.index("java"))

#Pop, retira objetos da lista (listas em python sao pilhas)

print(linguagens.pop())
print(linguagens)

#Reverse, espelha a lista

linguagens.reverse()
print(linguagens)

#Sort, ordena a lista em ordem alfabetica

linguagens.sort()
print (linguagens)

#Len, conta quantos objetos ah na lista

print(len(linguagens))