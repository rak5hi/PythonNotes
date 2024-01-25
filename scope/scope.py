name="rakshi"
count=1
color = 'black'
def another():
    color = "blue"
    global count
    count += 1
    print(count) 
    
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    
    print(f'{color}\n')
    greeting("rakshi")
    print(f'\n{color}')
    
    
another()