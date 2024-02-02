####################################################

class Connection:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('Connecting...')
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print('WARNING: There\'s already a connection')
            return cls.__instance
        
        def __init__(self):
            print('Connected to internet!')
            
connection = Connection()
connection2 = Connection()

print(connection == connection2)
#returns True bcz of __new__
#if we remove __new__ it returns False
print('\n\n')
####################################################

class Vehicle:
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)
    
    def __init__(self, wheels: int):
        self.wheels = wheels
        print(f'Initializing Vehicle with {wheels} wheels' )
  
class Motorbike:
    def __init__(self):
        print('Initializing Motorbike')
        
class Car:
    def __init__(self):
        print('Intializing Car')  
        
        
truck = Vehicle(16)
mb = Vehicle(2)
####################################################


#__new__ always return 
#__init__ not