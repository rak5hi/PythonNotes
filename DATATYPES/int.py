x=5        #...x=int("hdghs")-------ERROR  
y=int('6')   
result=y/x
print(result)   #...result is in float..1.2
    
print(type(result))
print(isinstance(x,int))

#using_underscore
x = 100_100_000
print(x)