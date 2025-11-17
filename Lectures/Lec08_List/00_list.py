n = 1000
numbers = list(range(n))

# 에라토스테네스의 체를 이용하여 소수를 구하라.
def make_prime_list(numbers, start, end):
    # 직접 짜게 해 주세요
    for i in range(start, end):
        # check this number is prime
        if numbers[i] != -1:
            # 이 값은 소수이다. 그 배수들을 모두 -1로 바꾼다.
            for 지울인덱스 in range(i * 2, end, i):
                numbers[지울인덱스] = -1

numbers[0] = -1
numbers[1] = -1
make_prime_list(numbers, 2, n)

while -1 in numbers:
    numbers.remove(-1)
print(numbers)

# 고수가 쓰는 코드
primes = [num for num in numbers if num != -1]
print(primes)


