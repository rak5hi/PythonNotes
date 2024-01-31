
def _dict():

    _dict = { "key1": "value1",
             "key2": "value2"}
    print(_dict)

    _dict1 = dict(key1="value1",key2="value2")
    print(_dict)

    print(type(_dict))
    print(len(_dict))

def access_item():
    
    _dict = { "key1": "value1",
             "key2": "value2"}
    
    print(_dict["key1"])
    print(_dict.get("key1"))
    #print(_dict.get('x')) ----output--NONE
    print(" ")
    
    print(_dict.keys())
    print(_dict.values())
    print(" ")

    print(_dict.items())
    print(" ")
    
    print("key1" in _dict)
    print("key2" in _dict)
    
    
def oper():
    
    _dict = { "key1": "value1", 
             "key2": "value2"}
   
    n = "\n"
    _dict["key1"] = 'a'
    _dict.update({"key2": 'b'})
    
    print(_dict)

    _dict["key3"] = 'c'
    
    print(_dict,n)
    
    print(_dict.pop("key2"),n)
    print(_dict)
     
    print(_dict.popitem(),n)
    print(_dict)
    

def dlt():
    
    _dict = { "key1": "value1", 
              "key2": "value2" }
    print(_dict)
    
    del _dict["key2"]
    print(_dict)
    
    _dict.clear()
    print(_dict)
    
    del _dict
#dlt()  
def copy():
    
    dict1 = { "key1": "value1", 
             "key2": "value2"}
   
    #dict2 = dict1 ----both point to same value
    
    dict2 = dict1.copy()
    dict2 = dict(dict1)
    
    print(dict2)
    
def nest():
    
    person = {"name": "rakshi",
              "iq": "low"}
    
    pet = {"name": "siri", 
           "iq": "very low"}
    
    home = {"member1": person,
            "member2": pet}
    
    print(home)
    print("")
    print(home["member1"]["name"])
    
    users = {'user1': 'rakshi',
             'user2': 'siri',
             'items': {'apple': 10,
                       'bannana': 20}}
    
    print(users['items']['apple'])
    
#nest()

def ext():
    
    dict1 = {"key1": "value1", 
             "key2": "value2"}
    
    print(dict1.setdefault('key1', 'there is no such key'))
    print(dict1.setdefault('x', 'there is no such key'))
     #print(dict1['x'])  ---ERROR
     
    x = dict1.values()
    print(x)  
    
    y = list(dict1.values())
    #y = tuple(dict1.values()) ---to make output readable
    
    print(y)  
    
ext()
