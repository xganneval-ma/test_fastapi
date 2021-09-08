import aiohttp
import asyncio
import datetime

SENARIOS = [
    [[100, 100]] * 5,
    [[80, 50 ]] * 100,
    [[50, 70 ]] * 100,
]

URL = "http://localhost:9518/firstname?waiting_time=%s&count=%s"
CONCURENCY = 100


async def get_persons(waiting_time: int, count: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL % (waiting_time, count)) as resp:
            return await resp.json()


async def execute_senarios():
    start_time = datetime.datetime.now()
    for senario in SENARIOS:
        await asyncio.gather(
            *[
                get_persons(senari[0], senari[1])
                for senari in senario
            ]
        )
    total_time = datetime.datetime.now() - start_time
    print(total_time.total_seconds())

asyncio.run(execute_senarios())
