import asyncio


async def fetch_data(data: int) -> dict:
    print('Fetching data...')
    await asyncio.sleep(2)
    return {'data': data}

async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i)


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(counter())
    
    data: dict = await task1                        #await & return
    print(data)
    await task2
    
asyncio.run(main())   

####################################################

# asynchronous function are also referred to as co-routines,
# co-routine: is a function that can be suspended and resumed.

# keyword >> await << : wait for something to finish before moving on

####################################################

# async def main02():
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(counter())
    
#     data: dict = await task1
#     print(data)
    
""" both task1 and task2 run co-routinly,
    function is going to only wait for task1
    to finish,after that it hit print() & 
    after it exit from function.
    so it does not wait for task2 to finish """
    
# """output: Fetching data 
#            0
#            1
#            2
#            ('data': 123)"""  
####################################################

# async def main01():
#     await counter()
#     await fetch_data(404) 
    
""" its going to run and finish counter()
    then it going run fetch_data() """
####################################################
