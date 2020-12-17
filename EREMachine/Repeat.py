from Empty import Empty
from Concat import Concat
from Epsilon import Epsilon
class Repeat:

    @staticmethod
    def getERE(child, num):
        if num < 1:
            return Empty()
        elif num == 1:
            return child
        else:
            ret = Concat(child, child)
            for i in range (2, num):
                ret = Concat(child, ret)

            return ret
