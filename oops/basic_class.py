####################################################

class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def moves(self):
        print("Moves along...\n")
        
    def get_model(self):
        print(f'{self.name.upper()}-----MODEL[{self.model}]')
        
####################################################
        
my_car = Vehicle('Tesla','model 3')
my_car.get_model()
my_car.moves()

####################################################
class Airplane(Vehicle):
    def __init__(self, name, model,faa_id):
        super().__init__(name, model)
        self.faa_id = faa_id
        
    def moves(self):                 #overriding moves() 
        print('Files along...\n')
            
class Bike(Vehicle):
    pass

####################################################

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')    

duke = Bike('Super-Duke','1200')    
xsr = Bike('Yamaha-XSR', '700')

cessna.get_model()
cessna.moves()
duke.get_model()
duke.moves()
xsr.get_model()
xsr.moves()

print('\n\n')
####################################################

my_car.name = "Supra"
my_car.model = 'MK4'

####################################################

for v in [my_car, cessna, duke, xsr]:
    v.get_model()
    v.moves()
    
####################################################
