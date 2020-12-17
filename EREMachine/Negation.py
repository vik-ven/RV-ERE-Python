from EREDef import ERE
from EnumImp import EREType

class Negation(ERE):
    @staticmethod
    def getERE(child):
        if child.getEREType == EREType.NEG:
            return child.children[0]
        else:
            return Negation(child)
    def __init__(self, child):
        self.hash = 0
        self.children = [child]

    def getEREType(self):
        return EREType.NEG

    def toString(self):
        return '~(' + self.children[0].toString() + ')'

    def __copy__(self):
        return Negation(self.children[0])

    def containsEpsilon(self):
        return not self.children[0].containsEpsilon()

    def derive(self, s):
        return Negation(self.children[0].derive(s))