####################################################

status: int = 403

if status == 400:
    print('Bad request')
elif status == 403:
    print('Forbidden')
elif status == 404:
    print('Not found')
else:
    print('Something went wrong')
 
 
match status:
    case 400:
        print('Bad request...')
    case 403:
        print('Forbidden...')
    case 404:
        print('Not found...')
    case _:
        print('Something went wrong...')
 
print('\n')
####################################################
# PATTERN MATCHING

def color():
    color =(25, 56, 200)

    match color:
        case r, g, b:
            print("No alpha.")
        case r, g, b, alpha:
            print(f"Alpha is {alpha}")
#color()          
####################################################
 
def image_list():          
    user_input: str = input('command: ')
    #user_input = find image.jpg abcd.png xyz
    p_command: list[str] = user_input.split()

    print(p_command)

    match p_command:
        case ['find', *images]:
            print(f'Finding: {images}')
        case ['download', *iamges]:
            print(f'Downloading: {images}')
        case ['cancel' | 'delete', *images] if len(images) > 1:
            print(f'Deleting: {images}')
        case _:
            print('Command not recognised...')

#image_list()
# *image is going unpack everything after find/cancel.. 
#   and store in it.       
####################################################
