"""
Estruturas de repetição:
Sao estruturas utilizadas para repetir um trecho de codigo um determinado numero de vezes.
Esse número pode ser conhecido previamente ou determinado atravez de uma expressao logica
"""
# Estrutura FOR

texto = input("informe um texto: ")
VOGAIS ="AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print (".".join(letra))

"""
Funçao range
Range é uma funçao built-in do python, ela é usada para produzir uma sequencia de numeros
inteiros a partir de um inicio (inclusivo) para um fim (exclusivo). Se usarmos range(i,j)
sera produzido:
i,i+1,i+2,i+3,...,j-1

Ela recebe 3 argumentos: Stop(obrigatorio), start(opcional) e step(opcional)
"""
#Ex:

for numero in range(11):
    print(numero, end=".")

print ()

for numero in range(5,51,5):
    print(numero, end=".")

"""
Comando while
É usado para repetir um bloco de codigo varias vezes. Usado quando nao sabemos quantas vezes
o codigo deve ser executado
"""
