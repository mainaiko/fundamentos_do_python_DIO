"""
Parametros especiais
Por padrao, argumentos podem ser passados para uma função python tanto por posiçao
quando explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido
restringir a maneira pelo qual argumentos possam ser passados, assim um dev precisa apenas 
olhar para definição da funçao para determinar se os itens passados por posiçao, por posiçao e nome ou por nome
"""
#Ex:

def teste (pos1,pos2, / , pos_or_kwd, * , kwd1, kwd2):
    return f"{pos1},{pos2},{pos_or_kwd},{kwd1},{kwd2}"

"""
Antes da barra = apenas posicioanis
Apos a barra = posicionais e por chave
Apos o asterisco = apenas por chave
"""

teste_1 = teste("posiçao 1", "posiçao 2", pos_or_kwd= "chave ou posicao", kwd2="apenas por chave 2", kwd1="apenas por chave 1")

print (teste_1)

"""
Objetos de primeira classe
Em python funçoes sao objetos de primeira classe, com isso podemos atribuir funçoes a variaveis,
passa-las como parametro para funçoes, usa-las como valores em estrutura de dados(listas,tuplas,dicionarios,etc) e
usar como valor de retorno para uma funçao (closures)
"""
#Ex
def somar (a,b):
    return a + b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print (f"O resultado da operaçao {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)

"""
Escopo local e global
Dentro do bloco da funçao o escopo é local. Portanto alteraçoes ali feitas em
objetos imutaveis serao perdidas quando o metodo terminar de ser executado. Para
usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador
que a variavel que esta sendo manipulada no escopo local é global.
Essa Nao é uma boa pratica e deve ser evitada
"""
salario = 2000

#modelo certo
def salario_bonus(bonus, salario):
    salario += bonus
    return salario

print (salario_bonus(500,salario))
