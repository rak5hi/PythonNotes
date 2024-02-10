import multiprocessing as mp
from time_stuff import get_time
import functools
import time

""" Creating partial functioin with arguments already inserted."""

def func_a(param):
    time.sleep(2)
    return param

def func_b(param):
    time.sleep(2)
    return param

def func_c(param, param2):
    time.sleep(2)
    return param, param2

def map_func(func):
    return func()

@get_time
def main():
    print(f'Cores available: {mp.cpu_count()}')

    a = functools.partial(func_a, 'A')
    b = functools.partial(func_b, 'B')
    c = functools.partial(func_c, 'C', 'C2')
    
    with mp.Pool() as pool:
       results = pool.map(map_func, [a, b, c])
       print(results)
        
if __name__ == '__main__':
    main()
    
    
#OUTPUT:
"""
Cores available: 12
['A', 'B', ('C', 'C2')]
Time: 2.4749763002619147 seconds
"""