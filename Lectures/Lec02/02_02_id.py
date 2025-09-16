# 식별자 테스트

radius = 5
area = 3.14 * radius * radius
circumference = 2.0 * 3.14 * radius

print('반지름: ', radius, '면적: ', area, '둘레: ', circumference)

## 한글은 잘 인식이 되는가
반지름 = 7
면적 = 3.14 * radius * radius
둘레 = 2.0 * 3.14 * radius

print('반지름: ', 반지름,  '면적: ', 면적,  '둘레: ', 둘레)

## 그럼 어떤 변수 식별자가 안 되는가?

# invalid decimal literal
# 1_radius = 2.0
# 2_radius = 3.0

# invalid syntax : 특수 문자는 사용할 수 없다.
# ^hello = 'hello'

# 밑줄은 일반 문자와 동일하게 취급된다. 
_hello_ = 'hello'
print(_hello_)

# 숫자가 중간 이후에 나타나는 것은 OK
hello1 = 'hello'
hello2 = 'hi'
print(hello1, hello2)

# 대문자와 소문자를 섞어 쓰는 것도 오케이
thisMessageIsNotToBePrinted = 'asdfasdfasdfafd'
print(thisMessageIsNotToBePrinted)

this_message_is_not_to_be_printed = 'asdfasdfasdfadfafd'
print(this_message_is_not_to_be_printed)


# 공백이 들어가면 안됨
#my message = 'asdfasdfasdfadfafd'
#print(my message )

# 대소문자는 서로 구분됨
apple = 'apple'
Apple = 'pear'
print(apple + Apple)






















