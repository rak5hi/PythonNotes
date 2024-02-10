import multiprocessing as mp
from time_stuff import get_time
import time


"""pools: can be used to spread out multiple computations across 
cpu cores so that they run in parallel without programmer having to do anything else."""


def convert_to_x(number:int) -> str:
    time.sleep(2)
    return number * 'x'

@get_time
def main():
    print(f'Cores available: {mp.cpu_count()}')

    values: tuple[int, ...] = tuple(range(1, 13))
    
    with mp.Pool(processes=13) as pool:               #processes= limiter
        results: list[str] = pool.map(convert_to_x, values)
        print('Results:', results)
        
    
if __name__ == '__main__':
    main()


#OUTPUT:
"""Cores available: 12
Results: ['x', 'xx', 'xxx', 'xxxx', 'xxxxx', 'xxxxxx', 'xxxxxxx',
'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxxx']
Time: 2.620011799968779 seconds """


"""
    for values 1-13: it takes 2 sec
    for values 13-25: it takes 4 sec
    ...

with limiter: processes=4.

    for values 1-5: it takes 2 sec
    for values 5-9: it takes 4 sec
    ...
"""
