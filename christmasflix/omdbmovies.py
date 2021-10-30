import requests
import yaml
from pprint import PrettyPrinter
pp = PrettyPrinter()

BASE_URL = 'http://www.omdbapi.com/?s='
NOT_FOUND = 'Not found'


def search_movie(term):
    with open("C:\code\python3\last_christmas\christmasflix\config.yaml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    payload = {'apikey': cfg['api_key'], 's': term}

    return requests.get(BASE_URL, params=payload).json()


if __name__ == '__main__':
    movie_info = search_movie('home alone')
    for movie in movie_info['Search']:
        print(movie['Title'])

