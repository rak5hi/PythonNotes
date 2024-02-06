class NegativeException(Exception):
    """Raised if a value is below 0"""    

    def __init__(self, number: float, error_code: int):
        self.number = number
        self.error_code = error_code
        super().__init__(f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})', self.number, self.error_code)
    
    def __str__(self):
        return f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})'
    
    def custom_method(self):
        print((self.number, self.error_code), 'were used by the custom method')
    
try:
    raise NegativeException(-1, 555)
except NegativeException as e:
    print(e)
    print(e.args)
    e.custom_method()
    
#print(e): is now not printing .__init__(message) instead
#          it is printing return value from __str__method


#object serialization can be done by pickle module
#
#Exception class doesn't support serialization--
#   so use/add another dunder method for serialization
#      IF IT NEEDED
#    def  __reduce__(self):
#       return NegativeException, (self.number, self.error_code)

