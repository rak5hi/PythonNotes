
if 0:
    with open('sample.text') as file:
        text = file.read()
        print(text)
    
    
class File:
    def __init__(self, name: str):
        self.name = name
        
    def  __enter__(self):
        print(f'Opening {self.name}...')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing {self.name}...')
        
        
if __name__ == '__main__':
    with File('sample.text') as file:
        print(file.name)
        # text = file.read()
        # print(text)
        
    print('Done!')


#CONTEXT MANAGER:  create own functionality when entering a file 
#                 and exiting a file.
# OPEN : is also a context manager

# File: a context manager that created with own fumctionality
#          NOTE: file.read() is not defined in File