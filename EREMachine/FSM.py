from EREDef import ERE
from Symbol import Symbol
from Empty import Empty


class FSM:
    contents = {}
    match = set()


    @staticmethod
    def getFSM(input, events):
        return FSM(input, events)

    def __init__(self, input, events):
        self.start = input
        FSM.contents = {}
        FSM.match = set([])
        self.events = events
        self.number = {}
        self.count = 0
        self.generate(self.start)

    def generate(self, state):
        #recursively parse out state machines
        self.number[state] = "s" + str(self.count)
        self.count = self.count + 1
        trans = {}
        if state.containsEpsilon():
            self.match.add(state)
        self.contents[state] = trans
        for event in self.events:
            next = state.derive(event)
            if(next == Empty.getERE()):
                continue
            trans[event] = next
            if next in self.contents:
                continue
            self.generate(next)


    def printOut(self):
        print("s0 [")
        self.printTransition(self.contents[self.start])
        print("]")
        for state in self.contents:
            if state == self.start:
                continue
            print(self.number[state]+ " [")
            self.printTransition(self.contents[state])
            print("]")
        if len(self.match) == 0:
            return
        print("alias match = ")
        for state in self.match:
            print(self.number[state] + " ")
        print("end of matching states")
    def printTransition(self, trans):
        for s in trans:
            print(" " + s.toString() + " -> " + self.number[trans[s]])