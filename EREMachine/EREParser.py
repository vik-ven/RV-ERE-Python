import re
from Concat import Concat
from Empty import Empty
from Epsilon import Epsilon
from Kleene import Kleene
from Negation import Negation
from Or import Or
from Symbol import Symbol
from FSM import FSM

class EREMachine():

    def __init__(self, initerestring, events):
        #initial spec ERE to start from
        self.erestring = initerestring
        #all events relating to ERE
        self.events = events
        #dictionary of quick lookup terms
        self.t = r"\(|\)|\~|\&|\||\*|\+|epsilon|\^|empty|\w+"
        self.initERE = self.genERE()
        self.symbolist = [Symbol.stringToRef[i] for i in self.events]
        self.fsm = FSM.getFSM(self.initERE, self.symbolist)
        self.currstate = self.initERE
        self.violated = False
        self.reported = False
        self.state_string = "s0"

    def update_state(self, symstring):
        statesymbol = Symbol.getERE(symstring)
        if statesymbol not in self.fsm.contents[self.currstate]:
            self.violated = True
        else:
            self.currstate = self.fsm.contents[self.currstate][statesymbol]
            self.set_state_string()
            #print("Proceeding to state ") + self.fsm.number[self.currstate]
    def reset_state(self):
        #reset current state to initial state
        self.currstate = self.initERE
        self.violated = False
        self.reported = False
        self.set_state_string()
    def set_state_string(self):
        self.state_string = self.fsm.number[self.currstate]

    def report_out(self):
        self.reported = True

    def genERE(self):
        plist = re.findall(self.t, self.erestring)
        plist = EREMachine.parse(plist)
        return EREMachine.makeERE(plist, self.events)

    #take list result and generate ERE recursively from inner lists
    @staticmethod
    def makeERE(erlist, symbols):
        if type(erlist) is list:
            negflag = False
            orflag = False
            catflag = False
            andflag = False
            #need some initial ERE to make sure this works correctly
            currentERE = Empty()
            for ind, obj in enumerate(erlist):
                if obj == "*":
                    if ind == 0:
                        raise SyntaxError("Kleene closure must be after stuff")
                    currentERE = Kleene.getERE(currentERE)
                elif obj == "~":
                    negflag = True
                    continue
                elif obj == "|":
                    orflag = True
                    continue
                elif obj == "+":
                    catflag = True
                    continue
                elif obj == "&":
                    andflag = True
                    continue
                else:
                    if ind == 0|negflag:
                        currentERE = EREMachine.makeERE(obj, symbols)
                    elif orflag:
                        currentERE = Or.getERE([currentERE, EREMachine.makeERE(obj,symbols)])
                        orflag = False
                    elif catflag:
                        currentERE = Concat.getERE(currentERE, EREMachine.makeERE(obj, symbols))
                        catflag = False
                    elif andflag:
                        currentERE = Negation.getERE(Concat.getERE(Negation.getERE(currentERE),Negation.getERE(EREMachine.makeERE(obj, symbols))))
                        andflag = False
                    else:
                        currentERE = Concat.getERE(currentERE,EREMachine.makeERE(obj, symbols))
                    if negflag:
                        currentERE = Negation.getERE(currentERE)
                        negflag = False
            return currentERE

        else:
            if erlist == 'empty':
                return Empty.getERE()
            elif erlist == 'epsilon':
                return Epsilon.getERE()
            elif erlist in symbols:
                return Symbol.getERE(erlist)
            elif not erlist:
                return
            else:
                raise ValueError('Either you have used a symbol not tied to event, or epsilon/empty is misspelled')
    #recursively parse out parenthesis. Combine with function above to save computation, but doesn't probably matter much for initial time difference
    @staticmethod
    def parse(expr):
        def _helper(iter):
            items = []
            for item in iter:
                if item == '(':
                    result, closeparen = _helper(iter)
                    if not closeparen:
                        raise ValueError("bad expression -- unbalanced parentheses")
                    items.append(result)
                elif item == ')':
                    return items, True
                else:
                    items.append(item)
            return items, False

        return _helper(iter(expr))[0]

