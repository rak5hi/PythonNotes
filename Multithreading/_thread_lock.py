import threading
import time

"""lock: ensure that only one thread(amoung locked thread) is started and finished during that lock."""

lock = threading.Lock()

def counter(limit: int, name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i+1, sep=':')
        
        
def task1():
    lock.acquire()
    counter(5, 'T-1')
    lock.release()
    
    
def task2():
    lock.acquire()
    thread3 = threading.Thread(target=task3)
    thread3.start()
    counter(5, 'T-2')
    lock.release()
    
def task3():
    counter(5, 'T-3')
    
def task4():
    lock.acquire()
    thread5 = threading.Thread(target=task5)
    thread5.start()
    counter(5, 'T-4')
    #lock.release()
    
def task5():
    lock.acquire()
    counter(5, 'T-5')
    lock.release()

def main():
    thread = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread4 = threading.Thread(target=task4)
  
    thread.start()
    thread2.start()
    thread4.start()
    
    thread.join()
    thread2.join()
    thread4.join()

if __name__ == '__main__':
    main()
    
"""Adding lock to thread: 
to ensure that the locked thread need to be finished before the 
functions/threads that require the lock can continue with using the lock.
 
In simple worlds, if two threads are locked: 
they are not run concurrently,they run one after another.

NOTE: if there is a thread that is not locked then it has 
nothing to do wih locked threads,so its not going to wait for it.
"""