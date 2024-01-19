####################################################
def syn():
    
    for x in "siri":
        print(x)    
    
    print("\n\n")
        
#syn()
####################################################

def syn2(): 
    nums = [1,2,3,4,5]
    
    #for a in nums:
    #for anything in nums:
    #for only_variable in nums:
    for x in nums:
        print (x)
            
####################################################
      
def syn3():
    nums = [1,2,3,4,5]
    
    for x in nums:
        print(x)
        if x == 3:
            break
    
    print("")
    
    
    for x in nums:
        if x == 3:
            continue
        print(x)
        
        
#syn3()

####################################################
def for_range():
    
    for x in range(3):
        print(x)
     
    print("")   
    
    for x in range(1,4):
        print(x)
    
    print("")
    
    for x in range(5,51,5):
        print(x)
              
#for_range()


def for_else():
    
    for x in range(1,5):
        print(x)
    else:
        print(5)
        
    print("")
     
    for x in range(1,5):
        print(x)
        if x == 3:
            break
    else:
        print(5)
        
        
    print("")
    for x in range(1,5):
        if x == 3:
            continue
        print(x)
    else:
        print(5)


for_else()