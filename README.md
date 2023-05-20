# KOSS
KOSS Selection task
Task1 - downloads a page from https://reqres.in/api/users?page{el} where el is an element in arr = [1, 2, 3]
Task1_sync does the download synchronously using requests
Task1_asyncc does the download asynchronously using sessions from aiohttp

Task2 - asynchronously downloads pages from https://xkcd.com/{comic_id}/info.0.json where {comic_id} is a natural number from
1 to 200.

Task2 when done synchronously does the job in about 60-65 seconds but using 'asyncio' and 'aiohttp' modules, the same task is
done in about 1 - 1.7 seconds.
