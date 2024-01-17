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
    
def add():
    
    data = ['a','b','c','d']
    space = "\n"
    
    data += [0]
    print(data)
    
    print(data.pop())
    print(data.pop())
    print(data,space,space,space)
    
    
    data[1:1] = [0]            #insert in b/w 
    print(data,space)
    
    data[1:2] = ["x"]          #replace
    print(data,space)
    
    data[1:3] = [0]            #replace
    print(data,space)
    
    data[0:]=[0]               #replace
    print(data,space)
    
    data[0:0] = ['a','b','c','d']     #insert in b/w
    print(data,space,space,space,space)
    
    
    data[1:3] = [1,2,3] 
    print(data,space)
    data[1:3] = [0] 
    print(data,space)
    data[0:3] = [0] 
    print(data,space)
    
    data[:1]=['a','b','c']
    print(data,space)
add()