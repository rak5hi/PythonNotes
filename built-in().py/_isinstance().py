class Fruit:
    def __init__(self, name: str):
        self.name = name
        
        
        
if __name__ == '__main__':
    apple: Fruit = Fruit('Apple')
    bannana: Fruit = Fruit('Bannana')
    
    
    if isinstance(apple, Fruit):
        print('Apple is a Fruit')
    elif isinstance(apple, str):
        print('This is a string')


    print(isinstance(bannana, Fruit))
    print(isinstance('bannana',str))

        