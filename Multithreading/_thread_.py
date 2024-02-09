import threading
import time


"""GIL: Global Interpreter Lock: a lock that allows only one thread 
to hold control of the python interpreter at any given time. It ensures 
thread safety and make sure that only one thread running at any given point in time."""

"""Python: only one line of code/ only one thread is going to be able to execute
at any given time."""

"""AsyncIo: the task cooperatively decide which task should start next.
  threading: OS decides which task shoould be switched at which point of time."""

def process_data(name: str, count: int):
    print(f'Strating {name}...')
    
    for i in range(count):
        print(name, i + 1, sep=':')
        time.sleep(1)
        
if __name__ == '__main__':
    thread1 = threading.Thread(target=process_data, kwargs={'name':'Thread-1', 'count':5})
    thread2 = threading.Thread(target=process_data, args=('Thread-2', 5))
    
    thread1.start()
    #time.sleep(3)
    thread2.start()
    
    thread1.join()
    thread2.join()