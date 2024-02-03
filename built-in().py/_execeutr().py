#user_input: str = input('Your code: ')

user_defined_code = """
x = 10 
print(x)

for i in range(10):
    print(i, end=' ')
    
"""

exec(user_defined_code)

#using evaluate () throws ERROR
#print(eval(user_defined_code))


####################################################

#execute is an extrenely powerfull and dangerous function

#don't use random script in exe(),
# it may contain a code that can harm the device or u may get hacked

####################################################
