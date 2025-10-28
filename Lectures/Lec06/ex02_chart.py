
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'

x = np.linspace(-np.pi, np.pi, 100)

y1 = x**2
y2 = np.sin(x)
y3 = np.log(x)
y4 = np.tan(x)


plt.plot(x, y1, label = 'x**2', color='blue')
plt.plot(x, y2, label = 'sin(x)', color='red')
plt.plot(x, y3, label = 'log(x)', color='green')
plt.plot(x, y4, label = 'tan(x)', color='black')

## 장식
plt.title("간단한 그래프")
plt.xlabel('x (라디언)')
plt.ylabel('y 함수값')
plt.ylim(-5, 5)
plt.legend() # 범례
plt.grid(True)

plt.show()







