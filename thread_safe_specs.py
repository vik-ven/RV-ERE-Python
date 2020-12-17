from pythonrv import rv
#import init_machine_inc
import testmod

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

@rv.monitor(lock = testmod.lock_constr, inc = testmod.incr)
@rv.spec(level=rv.ERROR)
def FSM_spec_lock(event):
    global statemachine
    #stuff to uncomment if you want to print out all states to a statelog
    #f = open("statelog.txt", "a")
    #f.write(statemachine.state_string + " is current state from event " + event.called_function.name + " and violated is {}\n".format(statemachine.violated))
    #f.close()

    statemachine.update_state(event.called_function.name)
    if statemachine.violated and not statemachine.reported:
        statemachine.report_out()
        assert False, "A lock was not created before incrementing in a thread"