"""
O que é
Emcapsulamento é um dos conceitos fundamentais em prograçao orientada a objetos
eles descreve a ideia de agrupar dados e os metodos que manipulam esses dados em uma unidade
isso impoe restriçoes ao acesso direto a variaveis e metodos e pode evitar a modificaçao acidental de dados
sendoo possivel a variavel de um objeto so ser alterada pelo metodo desse objeto
"""

"""
Recursos publicos e privados
Em linguagens como Java e C++, existem palabras reservadas para definir o nivel de acesso aos atributos
e metodos da classe. Em python nao temos palavras reservadas, porem usamos por convençoes o nome do recurso
para definir se a variavel é publica ou privada
Definiçao
Publico = pode ser acessador de fora da classe
Privado = so pode ser acesado pela classe

publico/privado
Todos os recursos sao publicos, a menos que o nome inicie com underline. Ou seja, o interpretador
python nao ira garantir a proteçao do recurso, mas por ser uma convençao amplamente adotada na comunidade,
quando encontrarmos a variavel e/ou metodo com nome iniciado por underline, sabemos que nao deveriamos
manipular o seu valor diretamente, ou invocar o metodo fora do escopo da classe.
"""

class Conta:
    def __init__(self, nmr_agencia, saldo=0):
        self._saldo = saldo
        self.nmr_agencia = nmr_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

aiko = Conta(100)

"""
Property para que servem
Com o property() do python, voce pode criar atributos gerenciados em suas classes. Voce pode usar
atribustos gerenciados, tambem conhecidos como propriedades, quando precisar modificar sua implementaçao interna
sem alterar a API publica da classe
PEGA UM METODO E TRANFORMA EM UMA PROPIEDADE
"""

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  #Atribui valor de propriedade ao metodo def x
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1

    
foo_teste = Foo(10)
print (foo_teste.x)
foo_teste.x = 10
print (foo_teste.x)
del foo_teste.x
print (foo_teste.x)

"""
Teste e exemplo
"""

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome 
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome 
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
Aiko = Pessoa("aiko", 2001)
print (Aiko.nome, Aiko.idade)