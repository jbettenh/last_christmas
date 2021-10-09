import requests
import yaml


BASE_URL = 'http://www.omdbapi.com/?t='
NOT_FOUND = 'Not found'


def search_movie():
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    payload = {'apikey': cfg['api_key'], 't': 'a+christmas+carol'}

    response = requests.get(BASE_URL, params=payload)
    return response.text


if __name__ == '__main__':
    print(search_movie())