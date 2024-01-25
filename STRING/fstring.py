py = "Python"
oops = "Object-Oriented and Procedure Oreiented"
_dict = {'key1':"python",'key2':"Object-Oriented and Procedure Oreiented"}
num = 10


print("\n" + py + " is a " + oops + " language." + "\n")   #concatenating string

print("%s is a %s language.\n"%(py,oops))                  #%s formatting

print("{} is a {} language.\n".format(py,oops))            #string.format() method
print("{0} is a {1} language.\n".format(py,oops))

print("{1} is a {0} language.\n".format(oops,py))

print("{p} is a {o} language.\n".format(p=py,o=oops))
print("{p} is a {o} language.\n".format(p="python",o="Object-Oriented and Procedure Oreiented"))

print("{key1} is a {key2} language.\n".format(**_dict))

#f-string

print(f"{py} is a {oops} language.\n")

print(f"{py} is a {oops.title()} language.\n")

print(f"{_dict['key1']} is a {_dict['key2']} language.\n")

print(f'10*10 is {num*num}\n')





