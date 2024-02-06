import time

####################################################

def _time():
    start_time: float = time.perf_counter()

    for i in range(10**8):
        pass

    print("Hello!")
    time.sleep(1)

    end_time: float = time.perf_counter()

    print('Total time1:', end_time - start_time, 'seconds')

####################################################

def time_func(func):
    def wrapper():
        start_time2: float = time.perf_counter() 
        
        x = func()
        
        end_time2: float = time.perf_counter()    
        print('Total time2:', end_time2 - start_time2, 'seconds')
        return x
    return wrapper

@time_func
def hello():
    for i in range(200):
        pass

####################################################

def time_func_with_arg(func):
                 
    def inner1(*arg, **kwarg):
        start_time3: float = time.perf_counter()
         
        x = func(*arg, **kwarg)     
        
        end_time3: float = time.perf_counter()    
        print('Total time3:', end_time3 - start_time3, 'seconds')
        return x
        
    return inner1
    
@time_func_with_arg
def sum_two_numbers(a, b):
    return a + b
    
####################################################
   
if __name__ == '__main__':
    a, b = 3, 2
    
    _time()
    hello()
    print(sum_two_numbers(a, b))
    
    
#in time_fun removing wrapper():
# @time_func
# def hello():
#   for i in range(200):
#       pass
# the above run itself without calling it
#so  MUST USE INNER FUNCTION(& RETURN IT) IN DECORATOR FUNCTION