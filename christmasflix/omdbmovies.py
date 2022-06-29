import os
import requests

BASE_URL = 'http://www.omdbapi.com/'
NOT_FOUND = 'Not found'


def search_movie(term):

    payload = {'apikey': os.environ['OMDB_API_KEY'], 's': term}

    data = requests.get(BASE_URL, params=payload).json()

    return data


def get_movie_info(movie_id):

    payload = {'apikey': os.environ['OMDB_API_KEY'], 'i': movie_id}

    return requests.get(BASE_URL, params=payload).json()


if __name__ == '__main__':
    movie_info = search_movie('asdasdfc')
    print(movie_info)
    if 'Error' in movie_info:
        print(movie_info['Error'])
    else:
        for movie in movie_info['Search']:
            print(movie['Title'], movie['imdbID'])

        one_movie = get_movie_info(movie['imdbID'])
        print(one_movie)




