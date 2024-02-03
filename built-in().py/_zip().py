people = ('Rakshi', 'Siri', 'Yashu')
numbers = (10, 20, 30)

zipped = zip(people, numbers)

if 0:
    print(zipped,'\n')
    #print(list(zipped), '\n')

    print(tuple(zipped))
    #print(tuple(zipped))

if 0:
    for item in zipped:
        print(item)
        
    
if 0:
    #tuple unpacking
    for name, number in zipped:
        print(name, number, sep=':')


people2 = ('Rakshi', 'Siri', 'Yashu', 'xyz')

if 0:
    for item in zip(people, numbers, strict=True) :
        print(item)
        
    for item in zip(people2, numbers, strict=True) :
        print(item)
        #throws ERROR -bcz enven tuole size 4-3
        
        
letters = (':', ':', ':')

if 0:
    for i, j, k in zip(people, letters , numbers):
        print(i, j, k)
        
#zips take tuple and puts together
