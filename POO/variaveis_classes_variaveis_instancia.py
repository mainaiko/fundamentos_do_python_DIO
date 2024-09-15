"""
Oque é e como utilizamos
Todos os objetos nascem com o mesmo numero de atributos de classe e instancia. Atributos de instancia sao diferentes
para cada objeto (cada objeto tem uma copia) ja os atributos de classe sao compartilhados entre os objetos
Toda variavel de classe é atribuida logo apos a definiçao da classe
"""

class Estudante:
    escola = "DIO"#atributo de classe

    def __init__(self, nome, numero):#atributo de instancia
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero} - {self.escola})"
    
aiko = Estudante("Aiko", 52142)
fatima = Estudante("fatima", 58454)

print (aiko)
print (fatima)

