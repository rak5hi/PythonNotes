#extremely memory efficient bcz of no order(index)
###############################################

def _sets():
    nums = {3, 1, 2, 2}
    print(nums)
    print(type(nums))
    print(len(nums))
    print(2 in nums)
    #print(nums[0])---ERROR
    
    print("\n")
    
    data = {0, "rakshi", False, True, 1, 2}
    print(data)
    
    print("\n\n")
   
#_sets()
###############################################

def copy():
    nums = {1,2,3,4,5}

    nums2 = set(nums)
    # nums2 = set((1,2,3,4,5))
    # nums2 = set({1,2,3,4,5})
    # nums2 = set([1,2,3,4,5])
    print(nums2)
 
    print("\n\n")
    
#copy()
###############################################

def add():
    num1 = {1, 2}
    
    num1.add(3)
    print(num1)
    
    num2 = {4, 5, 6}
    # num2 = (4, 5, 6)
    # num2 = [4, 5, 6]
    
    num1.update(num2)
    #num1.update({4, 5, 6})
    #num1.update((4, 5, 6))
    #num1.update([4, 5, 6])
    print(num1)
    
    print("\n\n")
    

#add()
###############################################

def oper():
    a = {1, 2, 3}
    b = {3, 4 ,5}
    c = set(a)
    d = set(a)
    
    aub = a.union(b)
    #aub = b.union(a)
    #aub = a | b        #---bitwise or operator
    #a |= b
    print(aub)
    
    anb = a.intersection(b)
    print(anb)
    
    c.intersection_update(b)
    print(c)
    
    d.symmetric_difference_update(b)
    print(d)
    
#oper() 

###############################################

def froz():
    
   a = frozenset({1,2,3,4,5})
   
   a.add(4)    #---ERROR
   
#froz()

def ext():
    items = {'apple', 'bannana',10,2,True}
    
    items.remove(2)
    print(items)
    
    items.discard(10)
    print(items)
    
    #items.remove('ashgs')  #---throw ERROR
    items.discard('jkhfjd') #---DON'T throw ERROR
    
    items.pop()   #==remove randomly
    print(items)
    
    items.clear()
    print(items)
#ext()

def emptyset():
    
    a = {}
    print(type(a))
    
    b = set()
    print(type(b))
    
emptyset()