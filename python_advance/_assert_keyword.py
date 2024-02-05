def start_program(data: dict):
    assert isinstance(data, dict), 'Invalid JSON'
    assert data, 'No data found...'
    
    print('Program loaded successfully!')
    
if 0:
    json: dict = {'name': 'Siri'}
    start_program(data=json)
    
if 0:
    json: dict = {}
    start_program(json)
    
if 0:
    json: str = "ahsgdhj"
    start_program(json)
    
print(__debug__)

""" Triple quotation is known as dock string """

"""  __debug__: is set to be True for normal/debug mode
but it is False in optimization mode """

""" optimization mode: go to terminal set to change directory
cd to current file, and use >> python -O filename.py <<
its a cap o  """

""" why optimization mode: bc it going to exclude assert keyword,
and make program run faster """

""" WHEN COMPILING THE PROGRAM IT ALSO COMPILE DACKSTRING ,
 TEXT DOES TAKES MEMORY """
 
""" use >> python -OO filename << 
    TO EXCULDE ALL DOCKSTRING too
    why need to? --> it run the file fast and effective
    and also reduce file size """
    
""" IT'S LIKE
             if __debug__:
                assert ...
                assert ...
                
                '''all DOCKSTRING'''
"""