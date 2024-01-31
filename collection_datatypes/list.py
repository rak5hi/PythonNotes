#################################################

def _list():
    
    _list = ["rakshi",7,True]
    empty_list=[]

    print("rakshi" in empty_list)
    
    print(_list[0])
    print(_list[-1])
    
    print(_list[0:2])
    print(_list[1:])
    print(_list[-3:-1])
    
    print(len(_list))
    
#################################################
    
def add():
    
    data = ['a','b','c']
    n = "\n"
    
    data += ['d']
    print(data,n,n)
    
    #insert in b/w
    data[1:1] = [0]           
    print(data)
    
    data[1:1] = [1,2,3]     
    print(data,n,n,n)
    
    #replaceing 
    data[1:4] = ['&']            
    print(data)
    
    data[0:3] = ['*','*','*','*'] 
    print(data,n,n)
    
    data[1:] = [0]
    print(data)
    
    data[:1]=['a','b','c','d']
    print(data)

#################################################

def listfunc():
    data = ['a','b','c']
    
    data.append('d')
    print(data) 
    
    data.extend([0,"*",1])        #takes list/itsName as argument
    print(data)    
                  
    data.insert(2,'*')
    print(data)
    

    print(data.pop())
    print(data)
    
    data.remove('*')              #not remove multiple identical element 
    print(data)
    
    
    del data[4]
    print(data)
    del data[3:]
    print(data)
    
    data.clear()
    print(data)
    
    del data                     #dlt list
    
 #################################################   

def _sort():
    nums = [0,3,1,2]
    names = ["Siri","rakshi"]
    data = [1,"rakshi",False]

    names[1:1] = 'aA'          # == ['a','A']
    print(names)
    
    nums.sort()
    names.sort()
    #data.sort()----ERROR
    print(nums)
    print(names)
    
    print(" ")

    names.sort(key=str.lower)
    # names.sort(key=str.upper)
    print(names)

    print(" ")
    
    nums.reverse()
    # nums.sort(reverse=True)
    # print(sorted(nums,reverse=True))
    print(nums)

    print(" ")

    numscopy=nums.copy()
    # numscopy=list(nums)
    # numscopy=nums[:]
    print(numscopy)


def listcopy():
    nums=[1,2,3]
    
    numscopy=nums.copy()
    # numscopy=list(nums)
    # numscopy=nums[:]
    print(numscopy)
    
    mylist=list([1,2,3])
    print(mylist)
    
    # x=nums---x&nums refer to same point
    
#listcopy()

def ext():
    
    people: list[str] = ["Rakshi","siri"]
    print("siri" in people)
    people.pop(0)
    print(people)
ext()