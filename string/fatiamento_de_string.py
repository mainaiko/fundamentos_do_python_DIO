"""
Fatiamento de strings é uma tecnica utilizada para retornar substrings
(partes da string original), informando inicio (start), fim(stop) e passo
(step):
[start:stop[step]].
"""
nome = "Aiko Marques"

nome[0]
#"A"

nome[:4]
#Aiko

nome[1:5]
#iko M

nome[0:12:2]
#Ak aqe

nome[::-1]
#seuqraM okiA