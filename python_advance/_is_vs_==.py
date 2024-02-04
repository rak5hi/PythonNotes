class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def __eq__(self, other):
        return self.__dict__ ==other.__dict__
    
####################################################
    
if 0:
    fruit_a: Fruit = Fruit('Apple', 10)
    fruit_b: Fruit = Fruit('Apple', 10)
    
    print(f'a: {id(fruit_a)}, b: {id(fruit_b)}')
    print(f'fruit_a is fruit_b = {fruit_a is fruit_b}')
    print(f'fruit_a == fruit_b = {fruit_a == fruit_b}')

####################################################
   
if 0:
    _ = 500
    a = _ + 500
    b = 1000
    
    print(f'a: {id(a)}, b: {id(b)}')
    print(f'a is b = {a is b}')
    print(f'a == b = {a == b}')
    print(a, b)

####################################################
    
if 1:
   a = 10
   b = 10
   
   print(f'a: {id(a)}, b: {id(b)}')
   print(f'a is b = {a is b}')
   print(f'a == b = {a == b}')
   print(a, b)
     
####################################################
    