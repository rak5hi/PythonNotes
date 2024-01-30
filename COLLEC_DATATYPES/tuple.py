################################################

def _tuple():
    
    my_tuple = ()
    my_tuple = (1, 2)
    my_tuple = (0, "rakshi", 7.7)
    #my_tuple = tuple((0, "rakshi", 7.7))

    print(my_tuple, type(my_tuple))
    print(my_tuple[1])
    
#_tuple()
################################################

def tuple1():
    
    s = ("tuple")
    t1 = ("tuple",)
    t2 = "tuple",
    print(f'''{type(s)}
    {type(t1)}
    {type(t2)}
            ''')

#tuple1()
################################################

def tuple2():
    
    t1 = (1, 2, 3)
    
    t2 = t1 + (4, 5, 6)
    print(t1)
    
    t3 = t1 * 3
    print(t3)
    
# tuple2()
################################################

def t_mod1():
    tuple_list = (0, 1, 2, [3,4,5])
    print(tuple_list)
    
    #tuple_list[3] = '*' -----ERROR
    
    tuple_list[3][0] = ('*')
    print(tuple_list)

    tuple_list[3][0:] = '*'
    print(tuple_list)

#t_mod1()
################################################

def unpack():
    unpack = (1, 2, 3, 4, 5)
    
    (x, y, *z) = unpack
    print(f'{x}\n{y}\n{z}\n')

    (a, *b, c) = unpack
    print(f'{a}\n{b}\n{c}\n')

#umpack()
################################################

def tuple_methods():
    _tuple = ('a', 'b', 'c', 'd', 'b', 'b')
    
    print(len(_tuple))
    print(_tuple.count('b'))
    print(_tuple.index('b'))
    
#tuple_methods()   
################################################

def t_mod2():
    mytuple = ('a', 'b', 'c')
    print(mytuple)
    
    mylist = list(mytuple)
    mylist.append('d')
    
    newtuple = tuple(mylist)
    print(newtuple)
    
#t_mod2()
################################################
def ext():
    people = "siri", #() do not make it tuple
    people2 = ("siri")
    print(type(people) ,type(people2))
    
#ext()