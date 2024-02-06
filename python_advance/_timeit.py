import time
import timeit

def make_calculation(first: int, second: int):
    for i in range(10**3):
        pass
    
def do_something():
    for i in range(10):
        x: int = i ** i
         
def get_time(func: str, repeat: int,number: int) -> float:
    speed: float = min(timeit.repeat(func, repeat=repeat, number=number, globals=globals()))

    print(f'{func} --> {round(speed, 4)} sec (ran {repeat * number:,} times)')
    
    return speed

if __name__ == '__main__':
    a, b = 1, 2
    
    get_time("x = [i for i in range(100)]", repeat=10, number=10**5)
    get_time("do_something()", repeat=10, number=10**5)
    get_time("make_calculation(a, b)", repeat=10, number=10**5)
    
    
    
    
 
####################################################
    
#number: number of test to do
#repeat: number of time to repeat
#repeat=10 times  &  number=10**5 no of test
#          TOTAL: 10^6
####################################################

#paasing func1 in get_time():
#                   pass without ():  get_time(func1)
#                   paa with ()    :  get_time("func1()")
# the latter is best bcz: can able to pass func1 with argument
#why?:    I WANT TO timeit.rpeat() TO CALL THE FUNCTION,
#         but not want to call it before it reaches that line of code          

####################################################

#x = 1_000_000
# using >> :, << : print(f'{x:,})
# output:   1,000,000

####################################################

#why need globals: bc witout globals, it doesn't know where 
#  function is coming from and throws ERROR
#by including globals: global tells the function to import these func and 
#  variable and put them inside the testing function 