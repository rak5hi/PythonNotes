class Student:
    def __init__(self, name: str):
        self.__name = name
        
    @property
    # getter method
    def name(self):
        print('private attribute is accessed')
        return self.__name
    
    @name.setter
    #setter method
    def name(self, val: str):
        print('private attribute is modified')
        self.__name = val
        
        
if __name__=='__main__':
    
    siri: Student = Student('siri')
    print(siri.name,'\n')                   
    # @PROPERTY decorator is used to access self.__name 
    # by using .name 
    
    siri.name = "SIRI"
    print(siri.name,'\n')
    # @name.setter is used to modify self.__name
    
    
#variable - normal attribute
#_variable - protected attribute
#__variable - parivate attribute