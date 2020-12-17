from pythonrv import rv
import init_machine_inc
import testmod



@rv.monitor(lock = testmod.lock_constr, inc = testmod.incr)
@rv.spec(level=rv.ERROR)
def FSM_spec_lock(event):
    #f = open("statelog.txt", "a")
    #f.write(init_machine_inc.statemachine.state_string + " is current state from event " + event.called_function.name + " and violated is {}\n".format(init_machine_inc.statemachine.violated))
    #f.close()
    init_machine_inc.statemachine.update_state(event.called_function.name)
    if init_machine_inc.statemachine.violated and not init_machine_inc.statemachine.reported:
        init_machine_inc.statemachine.report_out()
        assert False, "A lock was not created before incrementing in a thread"