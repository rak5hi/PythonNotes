def multiline():
    singleline="line-1 line-2 line-3"
    multiline="""    line-1
    line-2
    line-3    """
    print(singleline)
    print(multiline)
    print(len(singleline))
    print(len(multiline))

##################


def esc_n():
#...print('It's Boring')-----ERROR
    print('It\'s Boring')
    print('\n')
    print('\\n')
    
    
multiline()