import json
import requests

# AVOID RUNNING

def fetch_data(*, update: bool = False, json_cache: str, url: str) -> dict:
    if update:
        json_data = None
    else:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                print('Fetched data from the local cache!')
        except(FileNotFoundError, json.JSONDecodeError) as e:
            print(f'No local cache found... ({e})')
            json_data = None
            
    if not json_data:
        print('Fetching new json data... (Creating local cache)')
        json_data = requests.get(url).json()
        with open(json_cache, 'w') as file:
            json.dump(json_data, file)
            
    return json_data

if __name__ == '__main__':
    api_url: str = "https://dummyjson.com/comments"
    cache_file: str = 'comments.json'
        
    data: dict = fetch_data(update=False,json_cache=cache_file,url=api_url)
    
    print(data)
  
#def func(*, a):
#   ...
# *: indicates a is passed in as kwargs only  

#  requests.get(url).json()
#  req get url as json