
####################################################

if 0:
    u = input('ENTER a number: ')

    try:
        num = float(u)
        print(num)
    except ValueError:
        print('Please enter a valid number')
    except Exception as e:
        print('something went wrong...', e)
            
####################################################

if 0:
    class negativeexception(Exception):
        ...
  
    #raise negativeexception
    """can just raise exception without TRY & EXCEPT,
    but TRY & EXCEPTION code block never reach"""
    
    try: 
        raise negativeexception
    except negativeexception as e:
        print(e)

#it does ntg ,but it does work as exception
#  using TRY & EXCEPT do ntg
#  but raising negativeeception can throw ERRPR-negativeexception

####################################################

if 1:
    class NegativeException1(Exception):
        """Raised if a value is below 0"""    

        def __init__(self, number: float, error_code: int):
            self.number = number
            self.error_code = error_code
            super().__init__(f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})')
        

    try:
        raise NegativeException1(-2, 909)
    except NegativeException1 as e:
        print(e)
        print(e.args)
        
#its going to print message given to base fun .__init__('message)    
####################################################

if 0:
    class NegativeException2(Exception):
        """Raised if a value is below 0"""    

        def __init__(self, number: float, error_code: int):
            self.number = number
            self.error_code = error_code
            super().__init__(f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})', self.number, self.error_code)
        

    try:
        raise NegativeException2(-3, 709)
    except NegativeException2 as e:
        print(e)
        print(e.args)
      
####################################################

#customException: create a class which is inherit from
#                 the >> Exception class <<

