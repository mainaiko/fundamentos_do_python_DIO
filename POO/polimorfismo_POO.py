"""
Polimorfismo
Na programaçao o mesmo nome de funçao(mas assinaturas diferentes) sendo usado para tipos diferentes
"""
#len é usado para contagens de elementos ou caracteres

len ("python")
len ([10,20,30])

#len é um exemplo de polimorfismo pois pode exercer funçoes diferentes 

"""
Polimorfismo em herança
Na herança, a classe filha herda os metodos da classe pai. No entanto, é possivel modificar um metodo em uma classe
filha herdada da classe pai. Isso é particulamente util nos casos em que o metodo herdado do pai nao se encaixa
perfeitamente na classe filha
"""
class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self):
        print ("Pardol voa")

class Avestruz(Passaro):
    def voar(self):
        print ("Avestruz nao voa")


def plano_de_voo (Passaro):
    Passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())