
import numpy as np

vector1 = [1, 2, 3]

vector2 = [2, 3, 4]

print(vector1)
print(vector2)

print(vector1 + vector2)

u = np.array(vector1)
v = np.array(vector2)
w = u+v

print(u, v, w)


#  x + 2y + z = 9
# 2x + 3y + 4z = 21
# 3x + y + 2x = 10

# A x = b

A = np.array(
     [ [1, 2, 1],
       [2, 3, 4],
       [3, 1, 2] ]
     )

b = np.array([9, 21, 10])

# A x = b 인 x를 구하라.


x = np.linalg.solve(A, b)

print(x)


A_역행렬 = np.linalg.inv(A)
print(A_역행렬)

x = A_역행렬 @ b
print(x)




























