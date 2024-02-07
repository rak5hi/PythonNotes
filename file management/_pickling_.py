import pickle

"""
#    text: str = 'text'
#    number: int = 10
#
#    with open('filename', 'w') as file:
#         file.write(text + '/n')
#         file.write(str(number) + '/n')
"""

"""
#    with open('filename', 'r') as file:
#        print(file.readlines())
#        print(file.read())
"""

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def describe_fruit(self):
        print(self.name, ':', self.calories)



"""
#    #creating obj fruit
#    fruit: Fruit = Fruit('Apple', 100)
#    
#    fruit.calories = 150
#    
#    with open('save.pickle', 'wb') as file:
#        pickle.dump(fruit, file)
""" 
if 1:     
    with open('save.pickle', 'rb') as file:
        fruit: Fruit = pickle.load(file)
        
    print(fruit.name)  
    print(fruit.calories)
    
    fruit.describe_fruit()
    #print(fruit.describe_fruit())
     
    fruit.calories = 200
    
    fruit.describe_fruit() 
    
    
    
#PICKLING: process where a python object is converted into a byte stream.

#serializing the object: converting an object into a byte stream :SAVES data

# pickle.dump(fruit, file)
#  dump fruit in file.

#  DISCLAIMER:: PICKLE module is NOT SECURE
#            only unpickle data that can trusted