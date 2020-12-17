from EREDef import ERE
from EnumImp import EREType
from Epsilon import Epsilon
from Empty import Empty
#import your events function here

class Symbol(ERE):
    stringToRef = {}
    refToString = {}
    symbolnum = 1
    @staticmethod
    def getERE(name):
        #look a t the ref_to_string may need __hash__ imp => fixed in superclass maybe?
        if name in Symbol.stringToRef:
            return Symbol.stringToRef[name]
        else:
            newSymbol = Symbol()
            newSymbol.hash = newSymbol.__hash__() + Symbol.symbolnum
            Symbol.symbolnum = Symbol.symbolnum + 1
            Symbol.stringToRef[name] = newSymbol
            Symbol.refToString[newSymbol] = name
            return newSymbol

    def getEREType(self):
        return EREType.S

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.hash == other.hash
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def compare(self, object):
        if not isinstance(object, ERE):
            return -1
        if(object.getEREType() == EREType.S):
            return self.refToString[self] == self.refToString[object]
        return EREType.S == object.getEREType()

    def __copy__(self):
        return self

    def toString(self):
        return Symbol.refToString[self]

    def containsEpsilon(self):
        return False

    def derive(self, s):
        if(self == s):
            return Epsilon.getERE()
        else:
            return Empty.getERE()

