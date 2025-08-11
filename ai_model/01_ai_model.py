# 헬로월드 출력
text = '딥러닝'
print(f'hello {text}')

# 모델 버전 확인
# import tensorflow as tf
# print(tf.__version__)

# 평균 구하기
import numpy as np
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

x_avg = np.mean(x)
y_avg = np.mean(y)

print(f'x의 평균 {x_avg}')
print(f'y의 평균 {y_avg}')

# 기울기 공식의 분모 부분이다.
divisor = sum([(i - x_avg)**2 for i in x])

# 기울기 공식의 분자 부분이다.
def top(x, x_avg, y, y_avg):
  d = 0
  for i in range(len(x)):
    d += (x[i] - x_avg) * (y[i] - y_avg)
  return d
dividend = top(x, x_avg, y, y_avg)

# 기울기
a = dividend / divisor

# y절편
b = y_avg - (x_avg * a)

print(f'기울기 a = {a}')
print(f'y절편 b = {b}')

# 평균 제곱의 오차 구하기

# 1. 가상의 기울기 a 와 절편 b 정하기
fake_a = 3
fake_b = 76

# 2. 공부한 시간은 x, 실제 성적 y
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([72,83,77,82,88,92,95,97])

# 3. 평균 제곱  오차 구하기
def predict(x):
  return fake_a * x + fake_b

predict_result = []

for i in range(len(x)):
  predict_result.append(predict(x[i]))
  print(f'공부한 시간 = {x[i]}, 실제 성적 = {y[i]}, 예측 성적 = {predict(x[i])}')

# 결과 출력
n = len(x)
# y = 결과 y_pred = 예측값
def mse(y, y_pred):
  return (1/n) * sum((y-y_pred)**2)
print(f'평균 제곱 오차 mse = {str(mse(y, predict_result))}')