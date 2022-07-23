# c4cda9e7f889883ac40983a90e576b1b
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path = 'movie/76341'
params = {
    'api_key': 'c4cda9e7f889883ac40983a90e576b1b',
    'language': 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json()
print(response)
