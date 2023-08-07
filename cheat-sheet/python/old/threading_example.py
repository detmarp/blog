# see this: http://www.dabeaz.com/usenix2009/concurrent/



or this:
https://stackoverflow.com/questions/5127401/setdaemon-function-in-thread

import Queue
import threading

def basic_worker(queue):
    while True:
        item = queue.get()
        # do_work(item)
        print(item)
        queue.task_done()
def basic():
    # http://docs.python.org/library/queue.html
    queue = Queue.Queue()
    for i in range(3):
         t = threading.Thread(target=basic_worker,args=(queue,))
         t.daemon = True # so thread will quit when program ends
         t.start()
    for item in range(4):
        queue.put(item)
    queue.join()       # block until all tasks are done
    print('got here')

basic()

