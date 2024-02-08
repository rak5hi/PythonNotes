import asyncio

async def fetch_data(data: int) -> dict:
    print('Fetching data...')
    await asyncio.sleep(10)
    #return {'data': data}


async def main():
    task = asyncio.create_task(fetch_data(1))
    await asyncio.sleep(0.1)
    print('doing something')
    data: dict = await task        
    # await fot task1 to finish & assign the returned to data
    
    print(data)
    
#asyncio.run(main())
####################################################

"""task is wrapper of co-routine that schedules 
the co-routine to run the event loop as soon 
as possible.

as task is created: it's going to be queued 
to be run as soon as possible

task are non blocking"""

####################################################

""" task.done method """
""" task.result method"""

async def main2():
    task = asyncio.create_task(fetch_data(1))
    await asyncio.sleep(2)
    
    if task.done():
        data: dict = task.result()
        print(data)
    else:
        print('Data not ready...')     
   
        
asyncio.run(main2())