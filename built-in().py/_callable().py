a: str = 'a'

def do_something():
    pass

def b():
    ...
    

if __name__ == '__main__':
    print(callable(a), '\n')
    
    print(callable(do_something))
    print(callable(b), '\n')
    
    print(callable(b()))
    
    