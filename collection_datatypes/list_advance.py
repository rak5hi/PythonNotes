####################################################

def using_loop():
    sample_list = []
    sample_list2 = []
    
    for i in range(10):
        sample_list.append(i)
        
    for i in range(10):
        if i % 2 == 0:
            sample_list2.append(i)
          
    print(sample_list)
    print(sample_list2, end='\n\n\n')

#using_loop()
####################################################

def list_comprehension():
    
    # [reuslt for element in list]
    sample_list = [i for i in range(10)]
    
    sample_list2 = [i for i in range(10) if i % 2 == 0]
    #sample_list2 = [i * 2 for i in range(10) if i % 2 == 0]
    
    print(sample_list)
    print(sample_list2)

#list_comprehension()  
####################################################
  
def list_comprehension2():
    
    people: list[str] = ['Rakshi','Siri','Yashu']
    
    cap_people = [person.upper() for person in people]
    
    print(cap_people)
    
#list_comprehension2()
####################################################

def double_slice():
    
    numbers: list[int] = list(range(21))
    
    print(numbers[::3])
    print(numbers[10::3])
    print(numbers[10:16:3])
    print(numbers[10:])
    print(numbers[:10])
    print(numbers[:10] + numbers[10:])
    
#double_slice()
####################################################

def modify_in_loop():
    
    number: list[int] = [0, 1, 2, 3]
    
    for num in number:
        if num == 1:
            number.remove(1)
        
        if  num == 2:
            print('''after removing [1]--1,
                  index of 2--becomes[1],
                  nxt for loop iterate through [2]--3''')
            
        print(num, '-->' ,number)
    print("\n\n")
        
#modify_in_loop()
####################################################

def modify_in_loop2():
    
    number: list[int] = [0, 1, 2, 3]
    number2: list[int] = []
    
    for num in number:
        print(num, '-->' ,number2)
        
        if num == 1:
            pass
        else:
            number2.append(num)
        
        if  num == 2:
            pass

    print(number2)
    
#modify_in_loop2()
#  NEVER TRY TO change or edit the current loop 
#  that iteratung through bcz it will lead to 
#  unintended side effects.
####################################################

