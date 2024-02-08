import asyncio

async def fetch_data(data: int) -> dict:
    print('Fetching data...')
    await asyncio.sleep(2)
    
    if data == o:
        raise Exception('No data...')
    
    return {'data': data}

async def main():
    tasks = asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(0),
        return_exceptions=True
    )
    
    results = await tasks
    print(results)
    

asyncio.run(main())


"""NOTE: if there is a error, there is no result 
&  also API calls are wasted too .which cost money.
That's the reason:  return_exceptions=True is used.
"""