from functools import wraps
from time import perf_counter, sleep
from typing import Callable

#to use @wrap & time function
####################################################

if 0:
    #function can be treated as object
    def shout(text):
        return text.upper()

    yell = shout
    print(yell('Hello!'))
    
    def whisper(text):
        return text.lower()
    
    #function can be passed as argument
    def greet(func):
        greeting = func("hello")
        print(greeting, '...')
        
    greet(shout)
    greet(whisper)
    
####################################################

if 0:
    #function can return another function
    def create_adder(x):
        def adder(y):
            return x + y
        
        return adder
    
    add_15 = create_adder(15)
    
    print(add_15(10))

#NOTE: function returning function without parenthesis

####################################################

if 0:
    def hello_decorator(func):
        """inner() is a wrapper function
        in which argument is called"""
        def inner1():
            print('Befor...')
            func()
            print('After...')
            
        return inner1

    def function_to_be_used():
        print("Inside function!")
      
    a = hello_decorator(function_to_be_used)
    
    a()
    
####################################################
if 0:
    def hello_decorator2(func):
        
        def inner1(*arg, **kwarg):
            print('Befor Execution')
            x = func(*arg, **kwarg)
            print('After Execution')
            return x
        
        return inner1
    
    @hello_decorator2
    def sum_two_numbers(a, b):
        print("Inside the function")
        return a + b
    
    print('sum =', sum_two_numbers(1, 2))
####################################################

def get_time(func):
    """Times any function"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        func(*args, **kwargs)
        #print(args)
        end_time: float = perf_counter()
        
        total_time: float = round(end_time - start_time, 3)
        print('Time:', total_time, 'seconds')
        
    return wrapper

@get_time
#def do_something(param, key=123)
def do_something(param):
    """Do something important"""
    sleep(1)
    print(param)
 
if 0:   
    do_something('Hello') 
    print('__name__: ', do_something.__name__)
    print('__doc__: ', do_something.__doc__)
    
#NOTE: @wrapper is not neccessary
# with @wrapper: __name__:do_something & __doc__: Do something important
# without @wrapper: __name__: wrapper  & __doc__: None
# docstring: """ """
####################################################

# passing argument with @decorator

def repeat(times: int, message: str):
    """Repeat function call x amount of times"""
    
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = None
            print(message)
            for _ in range(times):
                value = func(*args, **kwargs)
             
            return value
            
        return wrapper
        
    return decorator
    
@repeat(2, 'HELLO!')
def func1():
    print('hello')

@repeat(2, 'NUMBERS!')    
def func2(a: int, b: int):
    print(a, b)
   

if 1:
    func1()
    func2(1, 2)
####################################################