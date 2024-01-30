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
        
        
do_math()