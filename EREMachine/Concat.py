from EREDef import ERE
from Empty import Empty
from Epsilon import Epsilon
from Or import Or
from EnumImp import EREType

class Concat(ERE):
    @staticmethod
    def getERE(left, right):
        cat = Concat(left, right)
        return cat.simplify()

    def __init__(self, left, right):
        self.hash = 0
        self.children = [left,right]

    def simplify(self):
        if self.children[0] == Empty():
            return Empty.getERE()
        elif self.children[1] == Empty():
            return Empty.getERE()
        elif self.children[0] == Epsilon():
            return self.children[1]
        elif self.children[1] == Epsilon():
            return self.children[0]
        else:
            return self
    def __eq__(self, other):
        return super(Concat, self).__eq__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def derive(self, s):
        left = self.children[0]
        right = self.children[1]
        if left.containsEpsilon():
            orChildren = []
            orChildren.append(Concat.getERE(left.derive(s), right.__copy__()))
            orChildren.append(right.derive(s))
            return Or.getERE(orChildren)
        return Concat.getEre(left.derive(s), right.__copy__())

    def getEREType(self):
        return EREType.CAT

    def toString(self):
        return '(' + self.children[0].toString() + ' ' + self.children[1].toString() + ')'

    def __copy__(self):
        return Concat(self.children[0], self.children[1])

    def containsEpsilon(self):
        for child in self.children:
            if not child.containsEpsilon():
                return False
        return True

    def derive(self, s):
        left = self.children[0]
        right = self.children[1]

        if left.containsEpsilon():
            orlist = [Concat.getERE(left.derive(s), right.__copy__()), right.derive(s)]
            return Or.getERE(orlist)
        return self.getERE(left.derive(s), right.__copy__())
