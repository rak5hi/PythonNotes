import multiprocessing as mp
from time_stuff import get_time
import time

""" starmap is used for passing multiple arguments into function."""

def add_numbers(*args) -> float:
    time.sleep(2)
    return sum(args)

@get_time
def main():
    print(f'Cores available: {mp.cpu_count()}')

    values = ((1, 2), (3, 4), (5, 6), (7, 8))
    
    with mp.Pool() as pool:
        results: list[float] = pool.starmap(add_numbers, values)               
        print('Results:', results)
        
    
if __name__ == '__main__':
    main()
    
    
#OUTPUT:
"""
Cores available: 12
Results: [3, 7, 11, 15]
Time: 2.4587574996985495 seconds
"""