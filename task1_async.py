import asyncio
import time
import aiohttp
import json

async def sdown():
    async with aiohttp.ClientSession() as session:
        for element in range(1, 4):
            print(f"Working on {element}")
            file = open("page" + str(element) + ".txt", "w")
            response = await session.get("https://reqres.in/api/users?page{el}".format(el=element), ssl = False)
            file.write(json.dumps(await response.json(), indent=4))
            file.close()
            print(f"Work {element} done ✅")
start = time.time()
    
asyncio.run(sdown())
print(time.time() - start)
