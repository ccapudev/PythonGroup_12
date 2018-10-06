class Ameba:

    version = '0.11'

    def __init__(self, name):
        self.name = name
        print("Creando Ameba")

    def mitosis_nativa(self, name):
        return Ameba(name)

    @classmethod
    def mitosis(cls, name):
        return cls(name)

class AmebaMejorada(Ameba):

    def __init__(self, name):
        self.name = name
        print("Creando Ameba mejorada")



ameba0 = Ameba("amb0")
ameba1 = ameba0.mitosis("amb1")

ameba0 = Ameba("amb0")
ameba1 = ameba0.mitosis_nativa("amb1")

ameba0 = AmebaMejorada("amb0")
ameba1 = ameba0.mitosis("amb1")
ameba1 = ameba0.mitosis_nativa("amb1")
