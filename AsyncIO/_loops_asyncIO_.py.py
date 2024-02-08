import asyncio


async def counter():
    for i in range(10**10):
        print(i)
        if i % 10_000 == 0:
            await asyncio.sleep(0.1)
        
async def main():
    task = asyncio.create_task(counter())
    
    await asyncio.sleep(2)
    task.cancel()
    print('Task cancelled')
    
    await task
    
    
asyncio.run(main())

""" break/pause is needed to start another co-routine,
bcz sometimes program might not actually have the 
time to consider it.(like in loops)"""