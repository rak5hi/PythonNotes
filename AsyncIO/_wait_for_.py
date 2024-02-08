import asyncio


async def fetch_data(data: int) -> dict:
    print('Fetching data...')
    await asyncio.sleep(6)
    return {'data': data}

async def main():
    task = asyncio.create_task(fetch_data(1))
    
    try:
        data: dict = await asyncio.wait_for(task, timeout=5)
        print(data)
    except asyncio.TimeoutError :
        print('Time out ERROR...')    
    
    
asyncio.run(main())