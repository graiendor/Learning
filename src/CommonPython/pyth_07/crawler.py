import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html, "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())