
# JSON: JAVASCRIPT OBJECT NOTATION

# its modeled to transfer data 

# its looks like dict

# used/seen in API request or any requests on the internet that require to get data

# easy to read and easy to refer to

import json

with open('file management/sample.json') as file:
    content: dict = json.load(file)
    print(content)


#NOTE: in json boolean expression is saved as false/true
#      when loading its going to pythonize it
#      means it converts to (True/False) readable in python