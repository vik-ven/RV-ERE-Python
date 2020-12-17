# Definitions for the basic ERE abstract class


class ERE(object):
    def __init__(self):
        self.children = []
        self.hash = 0
    def getEREType(self):
        pass
    def getChildren(self):
        return self.children
    def toString(self):
        pass
    def compare(self, object):
        if not isinstance(object, ERE):
            return -1
        if(self.getEREType() != object.getEREType()):
            return self.getEREType() == object.getEREType()

        objchildren = object.getChildren()
        for i in range(len(self.children)):
            result = self.children[i].compare(objchildren[i])
            if(result != 0):
                return result

        return 0

    def __eq__(self, other):
        if self.getEREType() != other.getEREType():
            return False
        objchildren = other.getChildren()
        for i in range(len(self.children)):
            if not (self.children[i] == objchildren[i]):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if self.hash != 0:
            return self.hash
        self.hash = self.getEREType()[1]
        for child in self.children:
            self.hash ^= child.__hash__()
        return self.hash
        #Figure out why they have super here for overridden hash fxn
    def __copy__(self):
        pass
    def __le__(self, other):
        return self.hash < other.hash
    def containsEpsilon(self):
        pass
    def derive(self, s):
        pass
    def getERE(self):
        pass

