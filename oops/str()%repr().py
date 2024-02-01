####################################################

class Bike:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
       
bike: Bike = Bike("super-duke-1200", 'black') 
print(bike)
print(bike.model, bike.color)
print(bike.__repr__()) 

print('\n')
####################################################

class Car:
    def __init__(self, model: str, color: str):
        self.model = model 
        self.color = color     
        
    def __str__(self):
        return f'{self.model} ({self.color})' 
    
    def __repr__(self):
        return f'representation of object'
        #by default it returns address
        
car: Car = Car("Supra-MK4", "black")
print(car)
print(car.__repr__())
####################################################
