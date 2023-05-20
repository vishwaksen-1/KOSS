import asyncio
import time
import requests
import json

async def s_down():
    for element in range(1, 4):
        print(f"Working on {element}")
        response = requests.get("https://reqres.in/api/users?page{el}".format(el=element))
        file = open("page" + str(element) + ".txt", "w")
        file.write(json.dumps(response.json(), indent=4))
        file.close()
        print(f"Work {element} done ✅")

start = time.time()
asyncio.run(s_down())
    
time_taken = time.time() - start
print('Time Taken {0}'.format(time_taken))
