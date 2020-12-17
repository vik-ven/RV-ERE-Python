from pythonrv import rv
import init_machine_six
import six



@rv.monitor(withclass=six.with_metaclass, add = six.add_metaclass)
def FSM_spec_lock(event):
    init_machine_six.statemachine.update_state(event.called_function.name)
    if init_machine_six.statemachine.violated and not init_machine_six.statemachine.reported:
        init_machine_six.statemachine.report_out()
        assert False, "Using with metaclass without first adding metaclass"


#@rv.monitor(addm=six.add_move, remove = six.remove_move)
#def FSM_spec_lock2(event):
#    init_machine_six.statemachine.update_state(event.called_function.name)
#    if init_machine_six.statemachine.violated and not init_machine_six.statemachine.reported:
#        init_machine_six.statemachine.report_out()
#        assert False, "add_move without matching remove_move"
