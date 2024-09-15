"""
O que é poo
É um paradigma de programaçao, que aplicado em python, java, c e etc
estrutura o codigo abstraindo problemas em objetos do mundo real, facilitando o entendimento
do codigo e tornando- o mais modular e extensivel.
Dois conceitos chave:
classes e objetos.
"""
#Conceito de classes e objetos

"""
Uma classe define as caracteristicas e comportamentos de um objeto, porem nao conseguimos usa-las
diretamente. Ja os objetos podemos usa-los e eles possuem as caracteristicas e comportamentos que
foram definidos nas classes.
"""

class Bicicleta:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        return f"BIBI"

    def correr(self):
        print ("Começando se mover")
        return f"Pegando velocidade"
    
    def parar(self):
        print ("Perdendo velocidade")
        return f"Parado"
    
    def __str__(self):
        return f"{self.__class__.__name__}: modelo={self.modelo}, ano={self.ano} e valor={self.valor}"
    """
    Maneira mais simplificada abaixo
    """
    def __str__(self):
        return f"{self.__class__.__name__}, {", ".join([f"{chave}={valor}"for chave,valor in self.__dict__.items()])}"

teste1 = Bicicleta("alu", 2021, 2500)

print (teste1)
print (teste1.correr())


