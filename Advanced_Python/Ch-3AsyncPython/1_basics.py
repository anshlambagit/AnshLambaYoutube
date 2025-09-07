import asyncio  
import time


async def process1():
    print("process-1 First Step") 
    await asyncio.sleep(6) # There can be an API call
    result = await process2()
    print("process-1 Second Step")
    print(f"process2 result {result}")

async def process2():
    print("process-2 First Step") 
    await asyncio.sleep(9) # There can be an API call
    print("process-2 Second Step")
    return "process-2 completed"

asyncio.run(process1())