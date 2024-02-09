import threading
import time

""" using with keyword """

#lock = threading.Lock()
sem = threading.Semaphore(5)


def process_something(id: int):
    with sem:
        print(f'{id} --> Running!')
        time.sleep(3)
        print(f'{id} --> Finished!')
         
    
    
if __name__ == '__main__':
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something, kwargs={'id': i + 1})
        thread.start()
        

""" like opening file with "with" keyword,with keyword can 
also used to open up a lock & execute the code inside that 
lock before releasing it naturally. """