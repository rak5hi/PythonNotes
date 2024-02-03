people: list[str, int] = ['Rakshi', 'Siri', 10, 'Yashu', 20]


def is_str(element):
    return isinstance(element, str)

def is_int(element):
    return isinstance(element, int)


filtered_people: list[str] = list(filter(is_str, people))

filtered_people_num: list[int] = list(filter(is_int, people))


print(filtered_people)
print(filtered_people_num, '\n\n')

print(filter(is_str, people))
print(type(filter(is_str, people)), '\n\n')

#print(list(filter(is_str(), people)))
#    ERROR
#         Don't use () for is_str inside filter


list_comprehension = [name for name in people if type(name) == str]

print(list_comprehension)

#it is best to use filter instead of list comprehension,
#bcz it is does'nt load entire object(list) into memory
#before using it 

#filter and map returns objects that are not complete lists,
#and thats why it need to be convert it to a list,bz they return an extremely #memory efficient version of what can be turned into a list or  which allows 
#to access the element one by one without loading the whole list into memory.
