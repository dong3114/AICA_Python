import numpy as np
import matplotlib.pyplot as plt

# 공부한 시간 x, 실제 성적 y
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

plt.scatter(x,y)
plt.show()

a = 0 # 기울기
b = 0 # 절편

lr = 0.03 # 학습률
epochs = 2001 # 반복횟수