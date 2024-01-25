####################################################

def syn():
    
    i = 1
    while i <= 10:
        print(i)
        i += 1
        
    print("\n\n")
    
#syn()        
####################################################
  
def cond():
    
    count = 1
    #while 1:
    #while 523:
    while True:
        print("while....")
        if count == 5:
            break
        count += 1
      
    print("\n\n")
              
#cond()
####################################################

def while_else():
    
    i = 1
    while i <= 10:
        print(i)
        i += 1
    else:
        print('''this is going to print...\nbcz we are exicting from while loop,\nafter cond becomes false...''')
        
        
    print("\n\n")
             
#while_else()
####################################################

def while_else2():
    
    i = 1
    while i <= 5:
        
        print(i)
        if i == 3:
            break
        i += 1
       
    else:
        print("this is not going to print ,bcz we are jumping outof loop using break.....")
        
    print("\n\n")
    
#while_else2()
####################################################

def while_else3():
    
    i = 0
    while i < 5:
        
        i += 1
        if i == 3:
            continue
        print(i)
       
    else:
        print("this is going to print ,bcz we are skipping the loop using continue.....")
        
    print("\n\n")
    
#while_else3()
####################################################


def p():
    print('syn')
    syn() 
    print("\n\n\n")
    
    print('cond')
    cond()
    print("\n\n\n")
    
    print("while else")
    while_else()
    print("\n\n\n")
    
    print("while else2")
    while_else2()
    print("\n\n\n")
    
    print("while else3")
    while_else3()
    
    
p()