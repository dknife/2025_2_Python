
from datetime import datetime

# [모듈 datetime] - << [클래스 datetime] : 내 클래스처럼 쓴다

############### D-day Counter

now = datetime.now()
print(f'오늘 날짜는 : {now.year}년 {now.month}월 {now.day}일입니다.')

print('목표일자를 입력하세요')

year =  int(input('연도'))
month = int(input('월:'))
day = int(input('일:'))

print(year, month, day)

target = datetime(year, month, day)

print(target)

gap = target - now

print(f'목표일까지 {gap.days}일 {gap.seconds // 3600}시간  남았습니다.')

