from multiprocessing import Pipe, Process, current_process
from random import randint
import os
import time


""" Using Pipes to send data or share data b/w two different Processes. """


def sender(connection):
    print(f'Sender: {current_process().name} ({os.getpid()})')

    for _ in range(5):
        rand: int = randint(1, 10)
        connection.send(rand)
        print(f'{rand} was sent...')
        time.sleep(0.5)
        
    
    print('Sending: "None"...')
    connection.send(None)
    #None is a sentinal value.
   
    print('Done with sending data!')
    
    
def receiver(connection):
    print(f'Receiver: {current_process().name} ({os.getpid()})')
    
    while True:
        data = connection.recv()
        print(f'{data} was received')
        
        if data is None:
            break
        
    print('Done receiving data...')
        
        
def main():
    c1, c2 = Pipe()
    
    s = Process(target=sender, args=(c2,))
    r = Process(target=receiver, args=(c1,))
    
    s.start()
    r.start()
    
    s.join()
    r.join()
    
    
if __name__ == '__main__':
    main()
    
"""None is a sentinal value.
Sentinel value is just a value that the receiver is going to wait
on to inform the process that there's no more values coming"""


#output:
"""
Sender: Process-1 (26112)
2 was sent...
Receiver: Process-2 (16692)
2 was received
4 was sent...
4 was received
6 was sent...
6 was received
7 was sent...
7 was received
5 was sent...
5 was received
Sending: "None"...
Done with sending data!     
None was received
Done receiving data...
"""
