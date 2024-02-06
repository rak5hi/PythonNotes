
# if a file in different folder specify its absolute path

with open('C:/Users/raksh/python/sample.text', 'r') as text:
    t: str = text.read()
    print(t)
    
    
with open('sample.text', 'r') as t:
    print(t.read(5))
    
    
with open('sample.text', 'r') as text:
    t1: str = text.readline()
    t2: str = text.readline()
    t3: str = text.readline()
    t4: str = text.readline()
    
    print(t1)
    print(t2)
    print(t3)
    print(t4)
 
    
with open('sample.text', 'r') as text:
    t: list[str] = text.readlines()
    
    print(t)
    
    
with open('sample.text', 'r') as text:
    print(text)
    
    
# reaed(): read all the lines in text
# read(5): read/gives/return specify amount of chararcter
# readline(): read only entire line
# readlines(): return list of lines