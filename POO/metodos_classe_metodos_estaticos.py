"""
Metodos de classe:
Estao ligados a classe e nao ao objeto. Eles tem acesso ao estado da classe, pois recebem um parametro que aponta
para a classe e nao para a instancia do objeto.
Por convençao chamamos de cls

Metodos estaticos:
Nao recebe um primeiro argumento explicito. Ele tambem é um metodo vinculado a classe e nao ao objeto da classe
este metodo nao pode acessar ou modificar o estado da classe. Ele esta presente em uma classe porque faz sentido
que o metodo esteja presente na classe.
"""
"""
Diferenças:
Um metodo de classes recebe um primeiro parametro que aponta para a classe, enquanto um metodo estatico nao.

Um metodo de classe pode acessar ou modificar o estado da classe enquanto um metodo estatico nao pode acessa-lo
ou modifica-lo
________________________________________________________________________________________________________________
Quando utilizar metodo de classe ou estatico:
Geralmente usamos o metodo de classe para criar metodos de fabrica 

Geralmente usamos metodos estaticos para criar funçoes utilitarias
"""
class Pessoa:
    def __init__(self, nome = None, idade= None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia ,nome):
        idade = 2024 - ano

        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade (idade):
        return idade >= 18


teste = Pessoa.criar_a_partir_data_nascimento(2001, 5, 1, "aiko")
print (teste.idade, teste.nome)
print (teste.e_maior_de_idade(21))