def do_math():
    user_input = input('ENTER a number: ')

    try:
        num = float(user_input)
        print(num)
    except ValueError:
        print('Please enter a valid number')
        do_math()
    except Exception as e:
        print('something went wrong...', e)
        
        
#do_math()

def user_input():
    
    user_input: str = input('ENTER: ')
    
    try:
        num = float(user_input)
        print(num)
    except Exception as e:
        print('Exception:', e)
    else: 
        print('Successfully executed code!')
    finally: 
        print('This will always run')
        #try:
             #.....
             
#user_input()

def _raise():
    is_connect: bool = False
    
    def connection():
        if not is_connect:
            #raise Exception("no internet!")
            raise ConnectionError("no internet!")
        else:
            print('connect to internet!')
            
    try:
        connection()
    except ConnectionError:
        print('There is no connection!')
    except Exception as e:
        print(e)
        
_raise()
        