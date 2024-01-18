import asyncio

async def getData():
    print("I'm here")
    await asyncio.sleep(2)
    print("I'm after 2 sec")


asyncio.run(getData())
