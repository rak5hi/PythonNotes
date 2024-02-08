import asyncio


async def main():
    await asyncio.sleep(0)
    print('Started!')
    result = await asyncio.sleep(1, results={'item':123})
    print(results)
    

if __name__ == '__main__':
    asyncio.run(main())
    
""" pssing 0 in sleep can also work as break,
aysncio.sleep(0) can be used in loops to 
create break/pause."""