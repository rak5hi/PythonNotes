names: list[str] = ['Siri', 'Rakshi', 'Python', 'xyz..']

for name in names:
    print(names.index(name) + 1, ':', name)
 
print('\n')   


for i in enumerate(names):
    print(i)
    
print('\n')   


for i, name in enumerate(names, start=1):
    print(i, ':', name)
    

#enumerate gives numbers to iterable

#looping through enumerate(names) gives tuple

#unpack the tuple using two variablr i,name