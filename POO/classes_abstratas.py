"""
O que sao interfaces
Interfaces definem o que uma classe deve fazer e nao como

Python tem interface?
o conceito de interface é definir um contrato, onde sao declarados os metodos (o que deve ser feito)
e suas respectivas assinaturas. Em python utilizamos classes abstratas para criar contratos. 
classes abstratas nao podem ser instanciadas
"""
"""
ABC
Por padrao, o python nao fornece classes abstratas. O python vem com um modulo que fornece a base para definir as classes abstratas, e 
o nome do modulo é ABC. O ABC funciona decorando metodos da classe base como abstratos e, em seguida registrando classes concretas como 
implementaçoes da base abstrata. Um metodo se torna abstrato quando decorado com @abstractmethod
"""
from abc import ABC, abstractmethod, abstractproperty

class Controle_remoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class Controle_TV(Controle_remoto):
    def ligar(self):
        print ("Ligando TV")

    def desligar(self):
        print ("Desligando TV")

controle = Controle_TV()
controle.ligar()
