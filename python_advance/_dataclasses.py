from dataclasses import dataclass

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

@dataclass
class Fruit2:
    name: str
    calories: float
    
if 1:
    apple: Fruit = Fruit('Apple', 10)
    apple2: Fruit = Fruit('Apple', 10)
    print(apple == apple2)

if 1:
    apple: Fruit2 = Fruit2('Apple', 10)
    apple2: Fruit2 = Fruit2('Apple', 10)
    print(apple == apple2)
    
if 1:
    apple: Fruit = Fruit('Apple', 10)
    apple2: Fruit2 = Fruit2('Apple', 10)
    print(apple == apple2)
    print(apple)
    print(apple2)