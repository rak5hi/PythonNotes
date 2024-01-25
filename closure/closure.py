####################################################
def parent(num):
    
    def inner():
        nonlocal num
        print(num/10)
        
    return inner

base10=parent(34)
base10()
####################################################

def non_closure(num):
    
    def inner():
        nonlocal num
        print(num/10)
        
    return inner()

_base10= non_closure(34)
#base10()
####################################################

def power(x):
    def inner(y):
        return y**x
    return inner

cube=power(3)
print(cube(5))
####################################################