import sys


####################################################


numbers: range = range(10)
numbers2: range = range(10**20)

print(numbers)

#type casting into list
print(list(numbers))

print(numbers2)
####################################################

print(range(2, 10, 2))
print(list(range(2, 10, 2)))
for i in range(2, 10, 2):
    print(i)
####################################################
print(list(range(0, -10)))  
print(list(range(0, -10, -2)))  
   
####################################################
   
print(sys.getsizeof(numbers))   
print(sys.getsizeof(numbers2))   

print(sys.getsizeof(list(numbers)))
print(sys.getsizeof(list(range(100)))) 
#print(sys.getsizeof(list(numbers2)))
      #ERROR --- too large to convert 
       
#print(list(numbers2))
    #ERROR --- too large to convert 
     
#for i in numbers2:
#     print(i)
#     
#no error -- but don't use it