from abc import ABC, abstractmethod

#ABC = abstract base class

####################################################
class Polygon(ABC):
    
    def poly(self):
        print("Im a Polygon")
        
    @abstractmethod
    def noofsides(self):
        ...

class Triangle(Polygon):
    
    #overriding abstractmethod
    def noofsides(self):
        print("Im a Triangle")
        
class ractangle(Polygon):
    
    #overriding abstractmethod
    def noofsides(self):
        print("Im a rectangle")
        
t = Triangle()
t.poly()
t.noofsides()
####################################################

class Phone(ABC):
    def __init__(self, model: str):
        self.model = model 
    
    def name(self):
        print(self.model.upper())
            
    @property
    @abstractmethod
    def color(self):
        ...
        
    @abstractmethod
    def description(self):
        ...
        
class Apple(Phone):
    @property
    def color(self):
        print("white")
        return ''
    
    def description(self):
        print(f'company-APPLE\nmodel-{self.model}\n')
        
mob1 = Apple("IPHONE11")
mob1.name()
print(mob1.color)
mob1.description()

####################################################

#propertymethod--always need to return something