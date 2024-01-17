import math

#####################################################

def name_type(name="rakshi"):
    print(type(name))
    print(type(name) == str)                     
    print(isinstance(name,str))
    
#str()----string constructor function

def Name_type(name="rakshi"):
    name=str(name)            #can cast numb to str
    print(type(name))
    print(type(name) == str)                     
    print(isinstance(name,str))
    
# name_type(1)---------class-int----f----f
# print("\n\n\n\n")
# Name_type(1)----class--str----t---t

#####################################################

#concatenation

def concatenation(x="rakshi",y=777):
#...conc=x+y.....error
    conc=x+str(y)
    print(conc)
    
#####################################################

def boolean():
    x=bool(True)
    y=True
    print(f'{x}\n{y}')
    print(isinstance(x,bool))
    


def integer():
    x=5        #...x=int("hdghs")-------ERROR  
    y=int('6')   
    result=y/x
    print(result)   #...result is in float..1.2
    
    print(type(result))
    print(isinstance(x,int))
    
#####################################################

def floating():
    x=6.6
    y=float(2.0)
    print(x/y)
    
    x=int(x)    #.....6
    x=float(x)   #.....6.0
    
#####################################################
    
def func():
    x=2.6
    y=-3
    print(abs(x))     #absolute function..
    print(abs(y))     #....3
    print(round(x))   #rounding to nearest integer.....3....for(2.5---2)
    print(round(y))   #...-3
    
#####################################################

def maths():
    print(math.pi)
    print(math.sqrt(64))
    print(math.ceil(2.6))    #......3
    print(math.floor(2.6))   #......
