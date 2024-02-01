####################################################

class Car:
    def __init__(self, model: str, color: str):
        self.model = model 
        self.__color = color
        self._version = 3

    def description(self):
        print('DISCRIPTION:')
        print(self.model, self.__color)
        self.__self_maintenance()
        
    def __self_maintenance(self):
        print(self.model, 'is Fixing itself...\n')
        
####################################################
   
car: Car = Car("supra-MK4", "Black")

#accessing attribute
print(car.model)
#print(car.__color)------ERROR
print('\n')

#accessing method
car.description()
#car.__self_maintenance()------ERROR

#accessing protected attribute outside CLASS
print(car._version)
print('')

####################################################

#__private attribut/method can only be accessed
# inside the Class
#but _protected can be accessed outside

####################################################

#THERE IS WAY TO ACCESSS PRIVATE ATTRIBUTE/METHODS
# OUTSIDE THE CLASS

print(car._Car__color)

car._Car__self_maintenance()

####################################################
