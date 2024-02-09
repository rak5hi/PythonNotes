import threading
import time

""" Semaphore is same like Lock.But run n threads at any given time."""

#sem = threading.Lock()
sem = threading.Semaphore(5)

def process_something(id: int):
    sem.acquire()
    print(f'{id} --> Running!')
    time.sleep(3)
    print(f'{id} --> Finished!')
    sem.release()
    
if __name__ == '__main__':
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something, kwargs={'id': i + 1})
        thread.start()
        

"""Difference b/w Lock() & Semaphore() -->

Lock(): at any instance only one thread are going to Run.
Semaphore(n): at any instance only n threads are going to Run.

seamphore(5): at any given time only 5 threads going to run.

Output of above code:
            its going to start/run 1 to 5,
            then 1 is going to release/finish 1,
            then 6 is going to start.....
            
bcz as thread-1 is finished there is one space left as the 
limit for number of threads running at any instance is 5.
"""