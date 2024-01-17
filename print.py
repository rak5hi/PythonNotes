def multiline():
    singleline="line-1 line-2 line-3"
    multiline="""    line-1
    line-2
    line-3    """
    print(singleline)
    print(multiline)
    print(len(singleline))
    print(len(multiline))

#################

def fullname(first="rakshith",last="gowda",initial="v"):
    fullName=first+last+initial
    print(fullName)
    
    fullName=first+" "+last+" "+initial
    print(fullName)
    
    fullName=first.title()+" "+last.title()+" "+initial.title()
    print(fullName)
    
##################

def esc_n():
#...print('It's Boring')-----ERROR
    print('It\'s Boring')
    print('\n')
    print('\\n')
    
    
esc_n()