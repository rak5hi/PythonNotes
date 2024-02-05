from functools import wraps
from time import perf_counter
import sys

def memoize(func):
    cache: dict = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key: str = str(args) + str(kwargs)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
    
        return cache[key]
    
    return wrapper

@memoize
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
if 1:
    start: float = perf_counter()
    f: int = fibonacci(36)
    end: float = perf_counter()
    
    print(f)
    print(f'Time: {end - start} seconds')
    

# fibonacci sequence is really tricky itself ,so first refer to that
# [1],[2],[3],[4],[5],[6]  == 0,1,1,3,5,8
# recursion: there is a limit set by default ,for amount of indepth recursion
#            if we use fibonacci(2000) >> don't try << >> try lesser number <<
#            it throws ERROR - recursion depth exceeded
# @memoize is used to reduce the time of excecution
#  WE DON'T NEED TO IMPLEMENT @MEMOIZE BY OWN

# we can use sys.setrecursionlimit(10_000) to set our own limit
#        >>> but DON'T USE IT <<<
