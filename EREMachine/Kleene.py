from EREDef import ERE
from EnumImp import EREType
from Concat import Concat

class Kleene(ERE):
    @staticmethod
    def getERE(child):
        return Kleene(child)

    def __init__(self, child):
        self.hash = 0
        self.children = [child]

    def getEREType(self):
        return EREType.STAR

    def toString(self):
        return self.children[0].toString() + '*'

    def __copy__(self):
        return Kleene(self.children[0].__copy__())

    def containsEpsilon(self):
        return True
    def derive(self, s):
        return Concat(self.children[0].derive(s), self.__copy__())