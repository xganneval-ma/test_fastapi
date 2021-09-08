from fastapi import FastAPI
import aiohttp
import asyncio
import datetime
from logging import getLogger
from pydantic import BaseModel
from operator import add
import functools

URL = "http://localhost:9518/firstname?waiting_time=%s&count=%s"

SENARIOS = (
    [[100, 100] for i in range(5)] +
    [[80, 50] for i in range(5)] +
    [[50, 70] for i in range(5)]
)


class Person(BaseModel):
    first_name: str
    birthdate: datetime.datetime
    gender: str


async def get_persons(waiting_time: int, count: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL % (waiting_time, count)) as resp:
            return await resp.json()

app = FastAPI()

logger = getLogger(__name__)


@app.get("/")
@app.get("/test")
async def data(count: int = 0):
    # return "toto"
    results = await asyncio.gather(
        *[
            get_persons(senari[0], senari[1])
            for senari in SENARIOS
        ]
    )
    persons = functools.reduce(add, results)
    persons = (Person(**person) for person in persons)
    persons.sort(key=lambda item: item.birthdate)
    return persons
