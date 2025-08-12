# 라이브러리 설정
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# 데이터 가져오기
Data_set = np.loadtxt('./data/ThoraricSurgery3.csv', delimiter=',')
print(type(Data_set))

# 예측 데이터와 결과 데이터 생성
X = Data_set[:, 0:16] # row전부를 가져오고, 0~16 개의 데이터를 가져온다
Y = Data_set[:, 16]   # row중에서 결과값이 들어있는 16 번째 컬럼 데이터를 가져옴

# 데이터 초기 분석 (Model 생성)
model = Sequential()
model.add(Dense(30, input_dim=16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 데이터 컴파일 과정
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X, Y, epochs=5, batch_size=16)

