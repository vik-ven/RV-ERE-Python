from EREDef import ERE
from EnumImp import EREType

#implementation of the empty set
class Empty(ERE):
    def __init__(self):
        self.children = []
        self.hash = 0
    @staticmethod
    def getERE():
        return Empty()
    def getEREType(self):
        return EREType.EMP
    def __eq__(self, other):
        return super(Empty, self).__eq__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def compare(self, other):
        if not isinstance(other, ERE):
            return -1
        return EREType.EMP == other.getEREType()
    def __copy__(self):
        return self
    def toString(self):
        return EREType.EMP[0]
    def containsEpsilon(self):
        return False
    def derive(self, s):
        return Empty()
