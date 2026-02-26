import asyncio
import aiohttp
from metrics import record

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.text()
        record(response.status)
        return data

async def run(url, total):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(total)]
        await asyncio.gather(*tasks)

def run_test(url, total):
    asyncio.run(run(url, total))
