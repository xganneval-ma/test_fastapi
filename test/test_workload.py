import timeit
import requests
ITERATION = 10
URL = "http://localhost:9600"


def test():
    requests.get(URL)


print(timeit.timeit(test, number=ITERATION) / ITERATION)
