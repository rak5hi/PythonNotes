from dataclasses import dataclass

if 0:
    people: list[str] = ['Siri', 'Rakshi']

    del people[1]

    print(people)

if 0:
    data: dict = {
        'field1': 100,
        'field2': 200
    }

    del data['field2']

    print(data)

if 0:
    name: str ='Rakshi'

    del name

    print(name)
    #ERROR - name is not defined

if 1:
    @dataclass
    class Fruit:
        name: str 
        calories: float
        
    apple: Fruit = Fruit('Apple', 30)

    print(apple, '\n')
    print(Fruit)
    
    del apple

    #print(apple)
    # ERROR
    
    del Fruit
    
    #print(Fruit)
    # ERROR