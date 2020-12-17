from pythonrv import rv
import init_machine_inc
import testmod

lockflag = False
reportflag = False
@rv.monitor(lock = testmod.lock_constr, inc = testmod.incr)
@rv.spec(level=rv.ERROR)
def FSM_spec_lock(event):
    global lockflag
    global reportflag
    if event.called_function.name == "lock":
        lockflag = True
    if event.called_function.name == "inc" and not lockflag:
        if not reportflag:
            reportflag = True
            assert False, "A lock was not created before incrementing in a thread"