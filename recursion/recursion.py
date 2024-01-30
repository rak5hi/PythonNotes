def add_one(num):
    
    if num >= 9:
        return num+1
    
    total=num+1
    print(total)
    
    return add_one(total)

 ###print(add_one(0))
#add_one(0)

def do_something(n: int):
    print(n)
    if n == 1:
        print("success!")
        return                       #work as BREAK KEY 
                                     # for func
    
    do_something(n-1)
    
#do_something(4)
 ###passing floating argument is ok, INT <--> FLOAT
 ###passing str argument -- ERROR