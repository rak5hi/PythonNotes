import asyncio


async def fetch_data(data: int) -> dict:
    print('Fetching data...')
    await asyncio.sleep(3)
    return {'data': data}


async def main():
    task = asyncio.create_task(fetch_data(1))
    await asyncio.sleep(2)
    
    task.cancel()
    await asyncio.sleep(0.1)            #NOTE-1
    print(task.cancelled())             #NOTE-2
    
    try:
        data: dict = await task
        print(data)
    except asyncio.CancelledError:
        print('Task was cancelled')
    
asyncio.run(main()) 


"""NOTE-1: this line is neccessary bcz without it
print(task.cancelled) is going return False.
REASON: in asynchronous everything happen so fast that 
task.canecl didn't have time to react
          
NOTE-2: Printing task.cancelled() NOT task.cancel """