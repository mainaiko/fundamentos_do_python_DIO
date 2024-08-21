"""
Em python 3 temos 3 formas de interpolar variaveis em strings, a primeira
é usando o sinal %, a segunda é utilizando o metodo format e a ultima é utilizando f strings.

Eu so uso f string
"""

nome = "Aiko"
idade = "23"
profissao = "Programador"
linguagem = "Python"

print (f"Ola , me chamo {nome}, eu tenho {idade} anos, trabalho como {profissao} e utilizo a linguagem {linguagem}")

# Formatar strings com f-string

PI = 3.14159

print (f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")