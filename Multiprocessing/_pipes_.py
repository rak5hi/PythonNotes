from multiprocessing import Pipe


""" Pipes: in Multiprocessing a pipe is a connection between 
two processes.It is used to send data from one process and 
to receive it with another process."""


def main():
    c1, c2 = Pipe()         #returns two ends of pipe
    #By default front(c1) is used for receiving & end(c2) to send.
    
    #TO send & receive data with both ends of the pipe.
    #c1, c2 = Pipe(duplex=True)
    
    c2.send('text')
    #only pickleable(hashable) obj can inserted/passed.
    
    print('Data to be received', c1.poll())        #c1.pool returns T/F
    obj = c1.recv()                                #if c1 is called & ntg has sent,its going to block(wait) the program.
    print(obj)
    print('Data to be received', c1.poll())


if __name__ == '__main__':
    main()
    
    
    
"""Processes by default do not share data with other processes.

Both pipes and queues can be used to send and receive
objects and data b/w processes.

Note: c1.recv() is going to wait/block unless its receive something.
if it not receive anything its going to wait and block rest of the program.
"""



