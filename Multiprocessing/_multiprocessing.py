
""" In Asyncio & Threading, code are executing concurrently.
How? : two or more caluculation are happening within the 
same time frame, but not at exact same time.
         
GIL: Global Interpreter Lock: Mechanism used in python interpreter
to synchronize the execution of threads so that only one native
thread can execute at a given time.

Multiprocessing: each process gets its own GIL, so its kind of 
get around that python restriction - of only being able to run
one thread at any given moment.

So with Multiprocessing: can run as many threads as wanted,
but its limited to the amount of cores present in a computer.

AsyncIo & Thread -> Concurrent.
Multiprocessing  -> Parallel. 

MultiThread   -> have different process id.
Multiprocess  -> have same process id."""