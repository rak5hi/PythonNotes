from time import sleep
from multiprocessing import Process, Lock, Semaphore
from time_stuff import get_time

def func(p_lock, identifier):
    with p_lock:
        sleep(1)
        print(f'>> Process {identifier} is running...')
        
        
@get_time   
def main():
    lock = Lock()
    sem = Semaphore()
    
    processes = [Process(target=func, args=(lock, i)) for i in range(5)]
    
    for process in processes:
        process.start()
        
        
    for process in processes:
        process.join()
        
        
if __name__ == '__main__':
    main()
    
#OUTPUT:
"""
>> Process 0 is running...
>> Process 1 is running...
>> Process 2 is running...
>> Process 3 is running...
>> Process 4 is running...
Time: 5.233223000075668 seconds
"""


""" with p_lock: 5 sec.
comenting/removing it: 1 sec. """
