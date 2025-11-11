import random as rnd

n = 100
r_list = [rnd.randint(1, n) for _ in range(n)]

print(r_list)

# 리스트를 정렬하고 싶어요
sorted = r_list.copy()
sorted.sort()
print(sorted)

for i in range(1, n):
    rep = sorted.count(i)
    print(f"{i} : {rep}개")

# 리스트에서 중복된 값을 제거하고 싶어요
print(min(r_list), max(r_list), sum(r_list))
print(min(sorted), max(sorted), sum(sorted))

print(sorted[::-1])