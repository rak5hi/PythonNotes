#user_input: str = input('Insert your maths: ')
user_input: str = "10 * 10 + 20"

result: float = eval(user_input)
print(result)


problem: str = """
10 * 'hello'
"""
print(eval(problem), '\n')



x: str = " print('Hello') "
print(eval(x))
#print() returns None


#print(eval('hello'))
#       ERROR

####################################################

#STATEMENT: doesn't return anything like print()
#EXPRESSION: it returns a value like (10 * 10), sum(10, 10)

####################################################
