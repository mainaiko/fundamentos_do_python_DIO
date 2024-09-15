"""
Metodo contrutor
Sempre é executado quando uma nova instancia da classe é criada. Nesse metodo
incializamos o estado do nosso objeto. Para declarar o medodo contrutor da classe, __init__
"""
class Cachorro:
    def __init__(self, nome, cor, acordado=True): #atributos da classe e os atributos sao as caracteristicas da classe
        print ("Inicilizando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

"""
Metodo destrutor
Destrutores em python nao sao tao necessarios quanto em C++ porque python tem um coletor de lixo
que lida com o gerenciamento de memoria automaticamente, __del__
"""

class Cachorro2(Cachorro):
    def __str__(self):
        return f"testando"

    def __del__(self):
        print ("Destruindo instancia")
    
c = Cachorro2("matheus", "dalmata")
print (c)

"""
o Incializador sempre vai ser executado primeiro.
"""