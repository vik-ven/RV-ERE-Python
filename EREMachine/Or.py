from EREDef import ERE
from EnumImp import EREType
from Empty import Empty

class Or(ERE):

    def __init__(self, childs):
        self.children = childs
        self.hash = 0
        assert(len(childs) >= 2)
    @staticmethod
    def getERE(childs):
        #return an ERE matching the OR after some simplifcation
        newOr = Or(childs)
        return newOr.simplify()
    def simplify(self):
        flattened = []
        previous = self.children
        changed = True
        while changed:
            changed = False
            flattened = []
            for child in previous:
                if(child.getEREType() == EREType.OR):
                    flattened.extend(child.getChildren())
                    changed = True
                else:
                    flattened.append(child)
            previous = flattened
        self.children = flattened
        self.children.sort()
        self.children = filter(lambda a: a != Empty.getERE(), self.children)
        j = 0
        while(j < len(self.children)-1):
            if self.children[j] == self.children[j+1]:
                del(self.children[j])
                j -= 1
            j +=1
        if len(self.children) == 0:
                return Empty()
        if len(self.children) == 1:
            return self.children[0]
        return self
    def getEREType(self):
        return EREType.OR

    def toString(self):
        ret = '(' + self.children[0].toString()
        for i in range(1, len(self.children)):
            ret += " | " + self.children[i].toString()
        ret += ')'
        return ret

    def __copy__(self):
        return Or.getERE(self.children[:])

    def containsEpsilon(self):
        for child in self.children:
            if child.containsEpsilon:
                return True
        return False

    def derive(self, s):
        newchildren = []
        for child in self.children:
            newchildren.append(child.derive(s))
        return Or.getERE(newchildren)