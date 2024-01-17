#############################

def name():
    name="Rakshi"
    print(name.lower())
    print(name.upper())
    print(name.replace('s','5'))
    print(name)
    
#############################

def multiline():
    
    multiline="""      
         rakshi
           """
    name="rakshi"
    print(len(name))
    print("")
    print(len(multiline))
    print("")
    
    print(len(multiline.strip())) #cuts the spaces
    print(len(multiline.lstrip())) #cuts the left spaces
    print(len(multiline.rstrip()))  #cuts the right spaces

#############################

def extra():
    name="rakshi"
    print(name.center(10, "."))  #10----length
    print(name.ljust(10, "."))   #left-(name)-----right-(.)
    print(name.rjust(10, "."))   #left-(.)----right- (name)
    print(name.rjust(10)) 
    print("Rakshi".rjust(10, ".")) 
#############################   

def fullname(first="rakshith",last="gowda",initial="v"):
    fullName=first+last+initial
    print(fullName)
    
    fullName=first+" "+last+" "+initial
    print(fullName)
    
    fullName=first.title()+" "+last.title()+" "+initial.title()
    print(fullName)
    
#############################

def strindex():
    
    name="rakshith"
    
    print(name[0])   
    print(name[-1])   
     
    print(name[0:6])   
    print(name[0:-2])   
    print(name[:-2])   
    
    print(name[:])   
    print(name[0:])   
    
