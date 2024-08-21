"""
Funçao é um bloco de codigo identificado por um nome e pode receber uma lista
de parametros, esses parametros podem ou nao ter valores padroes. 
Parametros sao a forma de entrada da funçao(entrada)
Funçao pode retornar varios valores(saida)
"""

def exibir_nome(nome):
    print (f"Bem vinda {nome}")

exibir_nome(nome="Aiko")
exibir_nome(nome="kamille")

"""
Retornando valores
para retornar um valor, utilizamos a palavra reservada return. Toda função python retorna NONE.
"""

def somar_numeros(numeros):
    return sum(numeros)

print (somar_numeros([12,4,5]))

def numero_sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print (numero_sucessor_antecessor(4))

"""
funções tambem podem ser chamadas usando argumentos nomeados da forma chave=valor
"""

def adcionar_carro(marca,modelo,ano,placa):
    return f"Carro adicionado com sucesso {marca}/{modelo}/{ano}/{placa}"

print (adcionar_carro(marca="fiat", modelo="MOBI", ano=2020, placa="ABC2424"))

"""
Args e Kwargs
Podemos combinar parametros obrigatorios com args e kwargs. Quando sao definidos (*args e **kwargs)
o metodo recebe os valores como tupla e dicionarios respectivamente
"""

