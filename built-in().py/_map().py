numbers: list[int] = [1, 2, 3, 4, 5, 6]

def convert_to_str(element):
    element *= element
    return str(element)

converted_list: list[str] = list(map(convert_to_str, numbers))

print(converted_list)

print(map(convert_to_str, numbers))
#filter and map returns objects that are not complete lists,
#and thats why it need to be convert it to a list,bz they return an extremely #memory efficient version of what can be turned into a list or  which allows 
#to access the element one by one without loading the whole list into memory.