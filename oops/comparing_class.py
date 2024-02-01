####################################################

class Car:
    def __init__(self, model: str, color: str):
        self.model = model 
        self.color = color

####################################################

class Bike:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color                                      
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
####################################################
    
    
if __name__ == '__main__':
        
    car: Car = Car("supra-MK4", "Black")    
    car2: Car = Car("supra-MK4", "Black") 
    
    print(car == car2)   
        
    bike: Bike = Bike("super-duke-1200", 'black') 
    bike2: Bike = Bike("super-duke-1200", 'black')
    
    print(bike == bike2)
    
    print('\n')
    
    print(car.__dict__)
    print(car2.__dict__, end='\n\n')
    print(bike.__dict__)
    print(bike2.__dict__)

