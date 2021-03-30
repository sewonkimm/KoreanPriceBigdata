import numpy as np
import pymysql
from datetime import datetime

# DB 연결
conn = pymysql.connect(host='j4a301.p.ssafy.io', port=3306, user='root', passwd='j301##', db='ssafy', charset='utf8')
cursor = conn.cursor()

target_ingredient_id = 2    # 예측 항목 ID
target_date = 3;            # 미래 예측 날짜, ex) 3일 후

# select 사용
sql = 'SELECT ingredient_avg_date, ingredient_avg_price FROM ingredient_avg WHERE ingredient_id = %s and DATEDIFF(SYSDATE(), ingredient_avg_date) <= 365 ORDER BY ingredient_avg_date'
val = (target_ingredient_id)
cursor.execute(sql, val)
result = cursor.fetchall()
# print(result)

# 트레이닝 데이터
x_train = np.array([])      # 날짜 (오늘 날짜 기준)
y_train = np.array([])      # 가격 (y원)

for i in range(len(result)):
    x_train = np.append(x_train, (result[i][0] - datetime.today().date()).days)
    y_train = np.append(y_train, float(result[i][1]))

print(x_train)
print(y_train)

# 가중치와 offset 초기화
W = 0.0     # 기울기
b = 0.0     # Y-절편

n_data = len(x_train)
epochs = 5000           # 전체 데이터에 대한 사이클 횟수
learning_rate = 0.01    # 경사하강법

for i in range(epochs):
    hypothesis = x_train * W + b                            # 예측 함수
    cost = np.sum((hypothesis - y_train) ** 2) / n_data     # 목적(비용) 함수, 평균 제곱 오차

    # W와 b의 오차 줄이기
    gradient_w = np.sum((W * x_train - y_train + b) * 2 * x_train) / n_data
    gradient_b = np.sum((W * x_train - y_train + b) * 2) / n_data

    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

    # Epoch print
    if i % 100 == 0:
        print('Epoch ({:10d}/{:10d}) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, epochs, cost, W, b))

# print('W: {:10f}'.format(W))
# print('b: {:10f}'.format(b))
print('오늘의 예측 가격 : ', x_train[-1] * W + b)              # 오늘의 예측 가격
print(target_date, '일 후 예측 가격 : ', target_date * W + b) # N일 후 예측 가격