from enum import Enum

####################################################
class State(Enum):
    OFF = 0
    ON = 1
    
state = State.ON

if state == State.ON:
    print('The lamp is turned on!')
    print(State.ON)
    print(State.ON.name)
    print(State.ON.value)
elif state == State.OFF:
    print('The lamp is turned off!')
    
print("",end='\n\n')
####################################################

class Color(Enum):
    RED = 'Red'    
    BLUE = 'Blue'
    GREEN = 'Green'
    
def check_color(color: Color):
    if color == Color.RED:
        print(color.name)
    elif color == Color.BLUE:
        print(color.name)
    elif color == Color.GREEN:
        print(color.name)
 
check_color(Color.RED)    

####################################################
# ENUM are user defined type
# ENUMs are used to create(represent) constant values,
# which will not change throught the program.
# caps letter used to represent consant variable
  