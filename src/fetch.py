import requests

def fetch(url: str) -> None:
    print('Fetching...')
    requests.get(url)
    print('Fetched!')