from EREDef import ERE
from EnumImp import EREType
from Empty import Empty
#implementation of the empty string
class Epsilon(ERE):
    def __init__(self):
        self.children = []
        self.hash = 0
    @staticmethod
    def getERE():
        return Epsilon()
    def getEREType(self):
        return EREType.EPS
    def __eq__(self, other):
        return super(Epsilon, self).__eq__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def compare(self, other):
        if not isinstance(other, ERE):
            return -1
        return EREType.EPS == other.getEREType()
    def __copy__(self):
        return self
    def toString(self):
        return "epsilon"
    def containsEpsilon(self):
        return True
    def derive(self, s):
        return Empty()
