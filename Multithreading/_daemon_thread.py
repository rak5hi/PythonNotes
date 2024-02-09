import threading
import time


"""Daemon thread: designed to only stay alive as long as there's 
 another thread(non-daemon) running."""


def infinite_loop():
    while True:
        print(time.time())
        time.sleep(1)
        
        
if __name__ == '__main__':
    thread = threading.Thread(target=infinite_loop, daemon=True)
    
    thread.start()      

"""Daemon threads are low priority threads.
They are used for some background tasks such as 
logging or periodically retrieving data.

As soon as all important threads are done functioning(or program is closed),
they will finish immediately.

Daemo threads are just low priority threads which do not prevent 
the system from existing unlike the important threads."""