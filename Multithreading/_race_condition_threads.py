import threading
import time

""" A race condition occurs when two threads access 
a shared variable at the same time. """


#lock = threading.Lock()


def edit(operation: str, amount: int, repeat: int):
    global value 
    
    #lock.acquire()
    
    for _ in range(repeat):
        temp: int = value
        time.sleep(0)          
        #giving opportunity to another thread for context switching
        
        if operation == 'add':
            temp += amount
        elif operation == 'subtract':
            temp -= amount 
            
    
        time.sleep(0)
        value = temp
       
    #lock.release() 
    
    
if __name__ == '__main__':
    value: int = 0
    
    adder = threading.Thread(target=edit, args=('add', 100, 1_000_000))
    subtractor = threading.Thread(target=edit, args=('subtract', 100, 1_000_000))
    
    adder.start()
    subtractor.start()
    
    print('Waiting for threads to finish...')
    
    adder.join()
    subtractor.join()
    
    print(f'value = {value}')
    

""" Excepcted value 0.

without Lock = getting crazy output 1_000_000,-998234...

with Lock = zer0 

bcz with Lock only one thread is going to edit."""