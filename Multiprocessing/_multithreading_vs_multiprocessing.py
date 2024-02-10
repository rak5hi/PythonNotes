import threading as t
from time_stuff import get_time, timestamp, kill_time
import os

def func(param):
    print(f'Strating: ({os.getpid()})...  ({timestamp()})')
    kill_time()
    print(f'{os.getpid()} finished! ({timestamp()})')
    
@get_time
def main():
    thread = t.Thread(target=func, args=('sample',))
    thread2 = t.Thread(target=func, args=('sample2',))
    
    thread.start()
    thread2.start()
    
    thread.join()
    thread2.join()
    
    
if __name__ == '__main__':
    main()
    
    
#OUTPUT:
"""
Strating: (21852)...  (12:57:36)
Strating: (21852)...  (12:57:36) 
21852 finished! (12:57:43)
21852 finished! (12:57:43)       
Time: 6.797822399996221 seconds 
"""

"""Thread & Asyncio is should be used more for
IO task or API request (or for sleep()).
bcz program is waiting on an external source"""

"""Multiprocessing is used for calculating some huge number."""