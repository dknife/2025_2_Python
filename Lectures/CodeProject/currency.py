import requests

url = 'https://open.er-api.com/v6/latest/USD'

response = requests.get(url)
print(type(response))

result = response.json()
print(type(result))

### 딕셔너리인 result를 이용해 보자.
# key를 던지면 value를 리턴한다.

print(result['result'])
print(f'현재 원달러 환율은 {result['rates']['KRW']}')
print(f'현재 엔달러 환율은 {result['rates']['JPY']}')
print(f'현재 위안달러 환율은 {result['rates']['CNY']}')