"""
Em programaçao herança é a capacidade de uma classe filha derivar ou herdar as caracteristicas
e comportamentos da classe pai(base)
Beneficios:
Representa bem os relacionamentos do mundo real
Fornece reutilizaçao de codigo repetidamente. alem disso permite adicionar mais recursos a uma classe sem modifica-la
É de natureza transitiva, o que significa que, se a classe B herdar a classe A,
todas as subclasses de B herdarao automaticamente a classe A.
"""
"""
Herança simples
"""
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        return f"Motor ligado"

    def desligar_motor(self):
        print ("Motor desligado")

class Moto(Veiculo):
    def __str__(self):
        return f"{__class__.__name__} {','.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"


class Carro(Veiculo):
    def __str__(self):
        return f"{__class__.__name__} {','.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"


class Carreta(Veiculo):
    def __init__(self, pergunta, cor, placa, numero_rodas):
        self.pergunta = pergunta
        super().__init__(cor, placa, numero_rodas)

    def __str__(self):
        return f"{__class__.__name__} {','.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"

    def esta_carregado(self):
        return f"{'Sim' if self.pergunta else 'Nao'} estou carregado"

moto_classica = Moto("Branco", "abc1230", 2)

print (moto_classica)
print (moto_classica.ligar_motor())

carro_classico = Carro("Preta", "bca321", 4)

print (carro_classico)
print (carro_classico.ligar_motor())

carreta_classica = Carreta("Vermelho", "asd456", 6, True)

print (carreta_classica)
print (carreta_classica.esta_carregado())