import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.schema import ingredient, ingredient_info, shopping_api, member, watch, ingredient_avg
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.linear_model import LinearRegression

router = APIRouter(prefix="/recommand")

@router.get('/latent/{id}')
def recommand(id: int, session: Session = Depends(db.session)):
    memberAll = session.query(member).all()
    index = []
    memberList = []
    ingredientList = range(1, 84)
    # 유저가 검색한 재료 리스트를 합쳐서 데이터프레임 생성
    for mem in memberAll:
        index.append(mem.member_id)
        w = []
        for i in range(1, 84):
            # 유저가 검색한 재료 별 횟수를 리스트로 저장
            query = session.query(watch).filter(and_(watch.member_id == mem.member_id, watch.ingredient_id == i))
            count = query.count()
            w.append(count)
        memberList.append(w)
    df = pd.DataFrame(memberList, index=index, columns=ingredientList).replace(0, np.NaN)
    columns = df.columns
    # 데이터 프레임을 행렬로 변환
    matrix = df.values
    print(matrix)
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

    # 사용자 행렬과 재료 행렬 합치기
    finalMatrix = np.dot(p, q.T)
    finalDf = pd.DataFrame(np.round(finalMatrix, 2), index=index, columns=columns)
    # 추천해줘야할 유저를 기준으로 데이터 추출 및 정렬
    recommend = finalDf.loc[[id], :].transpose().sort_values(by=[id], axis=0, ascending=False)

    # 결과값 도출(해당 유저에게 추천해줄만한 데이터(아직 조회하지 않은 재료 중))
    result = []
    for ingredient_id in recommend.index:
        if np.math.isnan(df.loc[[id], [ingredient_id]].values[0][0]):
            result.append(ingredient_id)
    data = []
    for ingredient_id in result[0:5]:
        query = session.query(ingredient).filter(ingredient.ingredient_id == ingredient_id)
        data.append(query.first())
    print(data)
    return data


@router.get('/predict/{ingredient_id}')
def predict(ingredient_id: int, session: Session = Depends(db.session)):
    # sql로 데이터를 받아서 데이터 프레임 생성
    df = pd.read_sql(session.query(ingredient_avg).filter(ingredient_avg.ingredient_id == ingredient_id).statement, session.bind)
    # 사용할 데이터 중 불필요한 Column 삭제
    del df['ingredient_avg_id']
    del df['ingredient_id']
    del df['ingredient_avg_previous_price']
    del df['ingredient_avg_predict_price']

    # 날짜를 사용할 수 있는 Int형으로 변환(현재 날짜 기준)
    df['ingredient_avg_date'] = (df['ingredient_avg_date'] - df['ingredient_avg_date'].max()).dt.days
    # 비어있는 데이터 삭제
    df = df.dropna()
    # 트레이닝 데이터
    x_train = df['ingredient_avg_date'].to_numpy()  # 날짜 (오늘 날짜 기준)
    y_train = df['ingredient_avg_price'].to_numpy()  # 가격 (y원)

    # 회귀 선형을 위한 라이브러리 객체 호출
    line_fitter = LinearRegression()
    line_fitter.fit(x_train.reshape(-1, 1), y_train)
    # 결과 값, 추후 DB에 저장할 예정
    print(line_fitter.predict([[x_train[-1] + 3]]))

    return
