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
   
_sets()
###############################################

def copy():
    nums = {1,2,3,4,5}

    nums2 = set(nums)
    # nums2 = set((1,2,3,4,5))
    # nums2 = set({1,2,3,4,5})
    # nums2 = set([1,2,3,4,5])
    print(nums2)
 
    print("\n\n")
    
copy()
###############################################

def add():
    num1 = {1, 2}
    
    num1.add(3)
    print(num1)
    
    num2 = {4, 5, 6}
    # num2 = (4, 5, 6)
    # num2 = [4, 5, 6]
    
    num1.update(num2)
    print(num1)
    
    print("\n\n")
    

add()
###############################################

def oper():
    a = {1, 2, 3}
    b = {3, 4 ,5}
    c = set(a)
    d = set(a)
    
    aub = a.union(b)
    #u = b.union(a)
    print(aub)
    
    anb = a.intersection(b)
    print(anb)
    
    c.intersection_update(b)
    print(c)
    
    d.symmetric_difference_update(b)
    print(d)
    
oper() 