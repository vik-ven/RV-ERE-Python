from pythonrvERE.EREParser import EREMachine

global statemachine

def initmachine():
    #Call this function first before you do anything

    # All ERE defined events in the form of string
    levents = ["add", "withclass"]
    #levents = ["addm","remove"]

    erestring = "(add (withclass)*)*"
    #erestring = "(addm remove)*"
    global statemachine
    statemachine = EREMachine(erestring, levents)