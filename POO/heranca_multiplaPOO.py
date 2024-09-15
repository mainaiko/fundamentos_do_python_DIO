"""
Herança multipla
"""

class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Cachorro(Mamifero):
    def __str__(self):
        return f"{__class__.__name__} {', '.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"


class Gato(Mamifero):
    def __str__(self):
        return f"{__class__.__name__} {', '.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"


class Ornintorrinco(Mamifero, Ave):
    def __str__(self):
        return f"{__class__.__name__} {', '.join([f'{chave}={valor}'for chave,valor in self.__dict__.items()])}"



gato_1 = Gato(nmr_patas = 4, cor_pelo="branco")
print (gato_1)

ornintorrinco_1 = Ornintorrinco(nmr_patas = 4, cor_pelo= "Marrom", cor_bico = "Preto")
print (ornintorrinco_1)