#need import of thread_safe to get rv it turns out
import thread_safe_specs
import threading
import logging
import time

import init_machine_inc
from pythonrv import rv
rv.configure(error_handler=rv.LoggingErrorHandler())
logging.basicConfig(filename="log",
        level=logging.ERROR,
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s")
from testmod import lock_constr, incr

i = 0
i_lock = threading.Lock()
def nsfw_test():
    global i
    for x in range(10000):
            i = incr(i)
def sfw_test():
    #use global variable i
    global i
    i_lock.acquire()
    lock_constr()
    try:
        for x in range(10000):
           i = incr(i)
    finally:
        i_lock.release()
def nsfw_function():
    #create 10 threads
    threads = [threading.Thread(target=nsfw_test) for t in range(10)]
    #for all threads, start
    for t in threads:
        t.start()
    #wait until all threads terminate
    for t in threads:
        t.join()

    print("The non-locked value of i is " + str(i))
def sfw_function():
    #same as above only using sfw w/ locking
    threads = [threading.Thread(target=sfw_test) for t in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("The safe value of i is " + str(i))

def main():
    start_time = time.time()
    #initmachine needs to be called to initialize global state machine. This needs to happen at some point
    init_machine_inc.initmachine()
    #init_machine_inc.statemachine.fsm.printOut()
    global i
    nsfw_function()
    i = 0
    init_machine_inc.statemachine.reset_state()
    sfw_function()
    print("--- %s seconds ---" %(time.time() - start_time))
if __name__ == '__main__':
    main()
