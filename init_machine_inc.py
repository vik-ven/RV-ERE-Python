from EREMachine.EREParser import EREMachine

global statemachine

def initmachine():
    #Call this function first before you do anything

    # All ERE defined events in the form of string
    levents = ["lock", "inc"]

    # erestring = "~(((inc | lock) (lock lock))*)"
    erestring = "(lock (inc*))*"

    global statemachine
    statemachine = EREMachine(erestring, levents)