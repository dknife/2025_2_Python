
import time

stime = time.time()


etime = time.time()

print(stime, etime)

# 1부터 10까지 더하고 그 값을 출력하는 데 걸리는 시간을 계산해 보라.

stime = time.time()
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
etime = time.time()

delta = etime - stime

print(f'1부터 10까지 더하고 그 값을 출력하는 데 걸리는 시간:{delta}초')


# 1부터 10까지 더하는 데에만 걸리는 시간을 계산해 보라.

stime = time.time()
res = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
etime = time.time()

print(res)

delta = etime - stime


print(f'1부터 10까지 더하는 데에만 걸리는 시간:{delta}초')


## 더하기 한 번에 걸리는 시간은??

iter = 100000

res = 0

stime = time.time()
for i in range(1, iter+1):
    res += i
etime = time.time()


delta = etime - stime
print(f'덧셈 한 번에  걸리는 시간:{delta / iter}초')

print(res)































