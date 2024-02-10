import multiprocessing as mp 
from time_stuff import get_time, timestamp, kill_time
import os

def func(param):
    print(f'Strating: {mp.current_process().name} ({os.getpid()})...  ({timestamp()})')
    kill_time()
    print(f'{os.getpid()} finished! ({timestamp()})')
    
@get_time
def main():
    process = mp.Process(name='Process-1', target=func, args=('sample',))
    process2 = mp.Process(name='Process-2', target=func, args=('sample2',))
    
    process.start()
    process2.start()
    
    process.join()
    process2.join()
    
    
if __name__ == '__main__':
    main()
    
       
#OUTPUT: 
"""
Strating: Process-1 (28292)...  (12:42:06)
Strating: Process-2 (32416)...  (12:42:06)
32416 finished! (12:42:10)
28292 finished! (12:42:10)
Time: 4.146058799698949 seconds
"""

"""output vary, sometimes both process finish at different speed."""

"""Thread & Asyncio is should be used more for
IO task or API request (or for sleep()).
bcz program is waiting on an external source"""

"""Multiprocessing is used for calculating some huge number."""