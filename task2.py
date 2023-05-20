import json
import time
import asyncio
import aiohttp

start = time.time()

def get_shit_done(session):
    tasks = []
    for i in range(1, 201):
        tasks.append(session.get("https://xkcd.com/{comic_id}/info.0.json".format(comic_id=i), ssl=False))
    return tasks

async def get_done():
    async with aiohttp.ClientSession() as session:
        tasks = get_shit_done(session)
        responses = await asyncio.gather(*tasks)
        for i in range(len(responses)):
            file = open("data" + str(i+1) + ".json", "w")
            response = responses[i]
            file.write(json.dumps(await response.json(), indent=4))
            file.close()

asyncio.run(get_done())

time_taken = time.time() - start
print('Time Taken {0}'.format(time_taken))