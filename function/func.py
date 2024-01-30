####################################################

def _func():
    print("hello")
    
#_func()
####################################################

def sum(num1,num2):
    if (type(num1) != int or type(num2) != int):
    #if type(num1) is not int or type(num2) is not int:
        return 0
    return num1+num2

#print(sum())------ERROR
#print(sum(2,3))
####################################################

#def sum2(num1,num2 = 0): ------IT WORKS
#def sum2(num1 = 0,num2): ----ERROR
               
####################################################

def sum2(num1=0, num2=0):
    
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2
    
# print(sum2()) 
# print(sum2(2,3)) 
# print(sum2(2,3.0)) 
####################################################

def multi_values(*args):
#def multi_values(*x):
    print(args)
    print(type(args))
    
#multi_values('a',1,True)
####################################################

def multi_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
#multi_items(key1= "rakshi", key2= "siri")
####################################################

def func_print():
    
    print("\n_func--")
    _func()
    print("\n")
    
    print("sum(2,3)--")
    print(sum(2,3))
    print("\n")
    
    print(f'sum2()--\n {sum2()}') 
    print(f'sum2(2,3)--\n {sum2(2,3)}') 
    print(f'sum2(2,3.0)--\n {sum2(2,3.0)}') 
    print("\n")
    
    print("multi_values--")
    multi_values('a',1,True)
    print("\n")
    
    print("multi_items--")
    multi_items(key1= "rakshi", key2= "siri")
    
#func_print()
####################################################

def place_holder():
    #to do things--
    pass


def pos_key(par1: str, par2: str = "Rakshi"):
    print(f'{par1}, {par2}')
  
#pos_key('Hello', par2 = 'siri')
  
##pos_key(par2 = 'siri', Hello) ---- ERROR--using position
## argument after keyworg argument

def sum_num(a: int, b: int) :
    pass
