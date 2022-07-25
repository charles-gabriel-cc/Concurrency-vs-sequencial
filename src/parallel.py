import time
from fetch import fetch
import concurrent.futures

def parallel(URL='https://jsonplaceholder.typicode.com/posts', threads=10, exec=100):
    time_start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as tpe:
        results = [tpe.submit(fetch, URL) for _ in range(exec)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    time_end = time.time()
    return round(time_end - time_start, 2)