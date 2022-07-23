import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path = 'movie/popular'
# path = 'movie/now_playing' 등 여러 방면으로 사용 가능
params = {
    'api_key': 'c4cda9e7f889883ac40983a90e576b1b',
    'language': 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json()
print(response)