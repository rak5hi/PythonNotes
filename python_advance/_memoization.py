import functools
from time import perf_counter
import sys

@functools.cache
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
if 1:
    sys.setrecursionlimit(501)
    start: float = perf_counter()
    f: int = fibonacci(499)
    end: float = perf_counter()
    
    print(f)
    print(f'Time: {end - start} seconds')
    
    
# 499 - default recursion depth limit
# to increase/set_our_own_limit use >> sys.setrecursion(limit) <<