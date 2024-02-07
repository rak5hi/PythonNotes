import json

####################################################
def j():
    with open('sample.json', 'r') as file:
        data: str = file.read()
        print(data, '\n')
        #print(data["name"]) -- ERROR
        #print(dict(data))  -- ERROR
        
        actual: dict = json.loads(data)
        print(actual)
        print(actual["person"]['name'])
  
#j()  
####################################################
    
def get_json(file: str) -> dict:
    with open(file, 'r') as file:
        actual: dict = json.load(file)
        return actual
    
sample_data: dict = get_json('sample.json')
print(sample_data)

####################################################

sample: dict = {'name':'Rakshi', 'age': 23, 'has_bike': None}

def sample_to_json():
    sample_json = json.dumps(sample)
    print(sample_json)
    
""" def sample_to_json_file():
        with open('sample.json', 'w') as file:
            json.dump(sample, file) 
            
DON'T NEED TO CONVERT TO JSON FILE, 
bcz some frameworks such as flask do it for us"""

sample_to_json()   
####################################################

#use json.load() for a file to convert
#use json.loads() for a string to convert
