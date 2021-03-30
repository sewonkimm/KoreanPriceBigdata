import sys
import pymysql
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

conn = pymysql.connect(host='j4a301.p.ssafy.io', port=3306, user='root', passwd='j301##', db='ssafy',
                       charset='utf8')
cursor = conn.cursor()


def memberWatch(mem):
    watch = []
    for index in range(1, 84):
        # 유저가 검색한 재료 별 횟수를 리스트로 저장
        sql = 'SELECT COUNT(*) FROM watch WHERE member_id = %s && ingredient_id= %s'
        cursor.execute(sql, (mem[0], index))
        count = cursor.fetchone()
        watch.append(count[0])
    return watch


def get_rmse(R, P, Q, non_zeros):
    Rt = np.dot(P, Q.T)

    # 실제 값에서 비어있지 않는 값과 같은 위치의 예측 값을 선택하여 RMSE 비교
    x_non_zero_idx = [non_zero[0] for non_zero in non_zeros]  # 행
    y_non_zero_idx = [non_zero[1] for non_zero in non_zeros]  # 열
    R_non_zeros = R[x_non_zero_idx, y_non_zero_idx]  # 실제 matrix의 NaN이 아닌 값들 선택
    Rt_non_zeros = Rt[x_non_zero_idx, y_non_zero_idx]  # 예측 행렬에서 똑같은 위치의 값들을 선택
    # 1차원의 array 2개 값들을 각각 비교
    mse = mean_squared_error(R_non_zeros, Rt_non_zeros)
    rmse = np.sqrt(mse)

    return rmse


def main():
    sql = 'SELECT member_id FROM member'
    cursor.execute(sql)
    result = cursor.fetchall()
    # mem = int(argv[1])
    index = []
    memberList = []
    ingredientList = range(1, 84)
    # 유저가 검색한 재료 리스트를 합쳐서 데이터프레임 생성
    for member in result:
        index.append(member[0])
        memberList.append(memberWatch(member))
    df = pd.DataFrame(memberList, index=index, columns=ingredientList).replace(0, np.NaN)
    columns = df.columns
    # 데이터 프레임을 행렬로 변환
    matrix = df.values
    num_members, num_ingredients = matrix.shape
    # 잠재요인 갯수
    K = 9

    # 난수 생성
    np.random.seed(1)
    # p : 사용자 - 잠재요인 행렬, q : 재료 - 잠재요인 행렬로 분해
    p = np.random.normal(scale=1. / K, size=(num_members, K))
    q = np.random.normal(scale=1. / K, size=(num_ingredients, K))
    # 행렬에서 값이 존재하는 값들 리스트에 저장
    non_zeros = [(i, j, matrix[i, j]) for i in range(num_members) for j in range(num_ingredients) if matrix[i, j] > 0]

    steps = 1000
    learning_rate = 0.05
    r_lambda = 0.0001

    # SGD 방법으로 p,q 행렬을 계속 업데이트(오차를 줄이기 위해)
    for step in range(steps):
        for i, j, v in non_zeros:
            err = v - np.dot(p[i, :], q[j, :].T)
            p[i, :] = p[i, :] + learning_rate * (err * q[j, :] - r_lambda * p[i, :])
            q[j, :] = q[j, :] + learning_rate * (err * p[i, :] - r_lambda * q[j, :])
            # rmse = get_rmse(matrix, p, q, non_zeros)  # 오차를 보기 위한 메소드
    # 사용자 행렬과 재료 행렬 합치기
    finalMatrix = np.dot(p, q.T)
    finalDf = pd.DataFrame(np.round(finalMatrix, 2), index=index, columns=columns)

    # 추천해줘야할 유저를 기준으로 데이터 추출 및 정렬
    recommend = finalDf.loc[[1], :].transpose().sort_values(by=[1], axis=0, ascending=False)

    # 결과값 도출(해당 유저에게 추천해줄만한 데이터(아직 조회하지 않은 재료 중))
    result = []
    for index in recommend.index:
        if np.math.isnan(df.loc[[1], [index]].values[0][0]):
            result.append(index)
    print(result[0:5])

    conn.close()


if __name__ == "__main__":
    main()
