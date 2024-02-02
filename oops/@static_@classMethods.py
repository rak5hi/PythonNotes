####################################################

class myClass:
    count = 0
    
    def __init__(self):
        self.x = 'x'
        
    @staticmethod
    def staticMethod():
        return "i am a static method"
    
    @classmethod
    def classMethod(cls):
        cls.count += 1
        
#staticmethod doesn't require self parameter

#classmethod can access and modify class variable.
#it takes class name as required parameter
####################################################

c1 = myClass()
print(c1.staticMethod())
print(myClass.count)
c1.classMethod()
print(myClass.count)

####################################################

class Calculator:
    def __init__(self, name: str):
        self.name = name
        
    def description(self):
        print(f'{self.name} is a a calculator!')
        
    @staticmethod
    def add_numbers(a: float,b: float):
        print( a + b)
        
    @classmethod
    def create_with_version(cls, name2: str, version: int):
        return cls(f'{name2}: ({version})')
      
#cls(f'{name2}: ({version})') == Calculator(name)  
#-it just converting 2 argument into str(1arg) to pass as (name)

####################################################
        
calc: Calculator = Calculator('BoB')
calc.description()

#add_numbers(2, 3)---ERROR
calc.add_numbers(1, 2)
Calculator.add_numbers(10, 20)

clac2: Calculator = Calculator.create_with_version("BoB", 100)
print(clac2.name)

####################################################
