import requests
city = 'Berlin'

url = f'https://wttr.in/{city}?format=3'

print(url)

weather = requests.get(url).text
print(f"현재 {city}의 날씨는 ", weather)