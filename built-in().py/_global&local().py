####################################################

var: str = 'GLOBAL'


class Fruit:
    def __init__(self):
        print('GLOBAL')
        

def hello():
    hello_str: str = 'str'
    
    def inner():
        pass
    
    print(locals())
    print(globals())
    print(locals() == globals())
    print("")
    
####################################################
    
if __name__ == '__main__':
    
    hello()
    print(locals() == globals())
    
####################################################

# globals(): even if it is used inside 
# func or class its is always refer to global
    
# locals(): if we use locals() in global field
# everything in global is refered as local

# globals() & locals() are exactly same at global level