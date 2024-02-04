def generate_list(n: int):
    for i in range(n):
        yield i
        
if 0:
    generator = generate_list(100)
    
    print(next(generate_list(100)), '\n')
    
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
  
if 0:
    generator2 = generate_list(3)
   
    print(next(generator2))
    print(next(generator2))
    print(next(generator2))
    print(next(generator2))
    # throws ERROR
    
if 0:
    generator3 = generate_list(100)
    
    list_x: list[int] = []
    for number in generator3:
        if number == 30:
            break
        list_x.append(number)
        
    print(len(list_x))#0-29
    print(list_x)
    
if 0:
    generator4 = generate_list(100)
    #instead of list(range(100))--this will immidiately create 100 number
    
    list_a: list[int] = []
    for number in generator4:
        list_a.append(number)
        if number == 9:
            break
    #generator_list release/create first 10 element
    
    print(list_a)
    print(next(generator4))
    
    list_b: list[int] = []
    for number in generator4:
        list_b.append(number)
        if number == 20:
            break
    #generator_list aleaready released upto num 10
    #so it going to release from 11 upto 20    
    print(list_b)
    
if 1:
    yield_comprehension = (i for i in range(100))    
    # DON'T CREATE LIST IMMIADIATELY
    # yield_comprehension = list(i for i in range(100))    
  
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))