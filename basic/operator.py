#OPERATOR

def comp():
    a = 2
    b= 8

    print(a < b and b < a)

    print(a < b or b < a)

    print(not(a < b or b < a))

#IDENTITY OPERATOR

def indentity():
    #is---identity operator
    a = 100
    b = 100
    
    print(id(a))
    print(id(b))
    
    print(a is b)
    print(a is not b)
    
#indentity()

def membership():
    #in---membership operator
    num = [1,2,3,4,5]
    
    print(1 in num)
    print(1 not in num)
    
#membership()