print('=====================================================')

# pip install requests
import requests
# URL로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답받은 값을 가져온다.
print(response, type(response)) # <Response [200]> <class 'requests.models.Response'>

# 속성 예시
print(response.status_code) # 200
print(response.text, type(response.text)) # 문자열

# 메서드 예시
# .json() 텍스트 형식으 json 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json())) # <class 'dict'>

print('=====================================================')

data = response.json()
# data는 딕셔너리 => key로 접근한다.
print(data.keys())
print(data.get('data').get('closing_price'))


