import time 
from fetch import fetch

def sequential(URL='https://jsonplaceholder.typicode.com/posts'):
    time_start = time.time()
    for _ in range(1000):
        fetch(URL)
    time_end = time.time()
    return round(time_end - time_start, 2)