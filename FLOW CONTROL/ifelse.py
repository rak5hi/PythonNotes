def age(age=24):

    if age > 18:
        print("you're too old")
    else:
        print("you're a child")
            
def ternary():
    
    #ternary operator---shorthand
    print("Success!") if 10 > 2 else print("Failure")
    
    a ,b = 20, 10
    
    result = a if a > b else b
    
    print(result)
    
    
ternary()

    

