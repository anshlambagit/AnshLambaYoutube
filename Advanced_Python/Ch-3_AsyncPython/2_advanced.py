import asyncio  
import time


async def process1():
    print("process-1 First Step")
    await asyncio.sleep(3) 
    print("process-1 Second Step")

async def process2():
    print("process-2 First Step") 
    await asyncio.sleep(6)
    print("process-2 Second Step")


async def main():

    tasks = await asyncio.gather(process1(), process2())

    print("Main Completed")


asyncio.run(main())
