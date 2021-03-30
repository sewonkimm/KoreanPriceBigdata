import urllib

import requests, bs4
import pandas as pd
from urllib.parse import urlencode, quote_plus, unquote
from fastapi import APIRouter, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from app.database.conn import db
from app.database.schema import ingredient, ingredient_info, shopping_api, member, watch
import time
import numpy as np
from sklearn.metrics import mean_squared_error

router = APIRouter()


@router.get("/")
def index():
    return {"about": {
        "/": "about",
        "/openApi": "openApi parsing",
        "/naverApi": "naverApi parsing"
    }}


@router.get('/openApi')
def openApi(session: Session = Depends(db.session)):
    xmlUrl = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'

    apiKey = unquote(
        '1J7amwxnHZ22NEowHAjGL9ihrCj%2FI%2BTvgjIesAJH%2F81p%2FJ0hI2qmYcKjcOrEfPkA0wXoVVgrzJHz4i1%2BRRxv6A%3D%3D')

    df_list = pd.date_range(start='20200602', end='20200603').strftime("%Y%m%d").tolist()
    ingredientAll = session.query(ingredient).all()

    for i in df_list:
        for ingred in ingredientAll:
            """
            openApi url과 함께 보낼 쿼리들을 urllib를 통해 생성
            """
            queryParams = '?' + urlencode(
                {
                    quote_plus('ServiceKey'): apiKey,
                    quote_plus('numOfRows'): '500',
                    quote_plus('pageNo'): '1',
                    quote_plus('examin_de'): i,
                    quote_plus('prdlst_cd'): ingred.ingredient_name_code
                }
            )
            """
            openApi 호출 후 데이터 받기
            """
            response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
            xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
            """
            데이터를 받기 위한 딜레이
            """
            time.sleep(0.5)
            """
            openApi 중 item만 받아오기
            """
            rows = xmlobj.findAll('item')
            """
            데이터가 없을 경우 다음 날짜로 이동
            """
            if not rows:
                continue
            rowList = []
            nameList = []
            columnList = []
            rowsLen = len(rows)
            """
            rows의 갯수만큼 반복해서 rowList에 저장
            """
            for i in range(0, rowsLen):
                columns = rows[i].find_all()
                columnsLen = len(columns)
                for j in range(0, columnsLen):
                    """
                    첫번째 columns에는 각 태그명이 들어있음
                    """
                    if i == 0:
                        nameList.append(columns[j].name)

                    eachColumn = columns[j].text
                    columnList.append(eachColumn)
                rowList.append(columnList)
                columnList = []

            """
            받아온 데이터를 데이터프레임으로 변경
            """
            result = pd.DataFrame(rowList, columns=nameList)
            """
            소비자 가격만 가져오고 혹시 도매 가격만 있다면 도매 가격으로 가져옴
            """
            if len(result[result['distb_step'] == '소비자가격'].index) > 0:
                result = result[result['distb_step'] == '소비자가격']
            """
            만약 디테일이 존재한다면 디테일 코드가 일치하는 데이터만 남기기
            """
            if ingred.ingredient_detail_name is not None:
                result = result[result['prdlst_detail_cd'] == ingred.ingredient_detail_name_code]
                if len(result.index) == 0:
                    continue

            """
            데이터를 DB에 저장
            """
            for index, data in result.iterrows():
                item = ingredient_info(ingred.ingredient_id, data['examin_de'], data['examin_amt'], data['examin_area_nm'], data['stndrd'])
                session.add(item)

        """
        한번에 commit, 만약에 저장할 때 중간에 에러가 발생한다면, 전부 rollback
        """
        session.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.get('/naverApi')
def naverApi(session: Session = Depends(db.session)):
    """
    네이버 Api 연동을 위한 id, secret
    encText을 사용하여 name으로 검색
    """
    client_id = "bYj15csqOZPThddA4ZSW"
    client_secret = "n0KSJICGeo"
    ingredientAll = session.query(ingredient).all()
    encText = ""
    for ingred in ingredientAll:
        if ingred.ingredient_detail_name is not None:
            encText = urllib.parse.quote(ingred.ingredient_detail_name)
        else:
            encText = urllib.parse.quote(ingred.ingredient_name)
        url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText + "&display=10&start=1&sort=sim"
        result = requests.get(url=url, headers={"X-Naver-Client-Id": client_id,
                                                "X-Naver-Client-Secret": client_secret})
        """
        받아온 데이터를 데이터프레임으로 변경
        필요없는 행 제거
        title에 검색한 이름은 태그가 붙어있어서 태그 제거
        """
        time.sleep(1)
        data = pd.DataFrame(result.json()["items"])
        data['title'] = data['title'].str.replace("</b>", "")
        data['title'] = data['title'].str.replace("<b>", "")
        """
        DB에 저장
        """
        for index, prod in data.iterrows():
            item = shopping_api(ingred.ingredient_id, prod['title'], prod['lprice'], prod['mallName'], prod['link'])
            session.add(item)

    session.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.get('/recommand/{id}')
def recommand(id:str, session: Session = Depends(db.session)):
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
    recommend = finalDf.loc[[1], :].transpose().sort_values(by=[1], axis=0, ascending=False)

    # 결과값 도출(해당 유저에게 추천해줄만한 데이터(아직 조회하지 않은 재료 중))
    result = []
    for index in recommend.index:
        if np.math.isnan(df.loc[[1], [index]].values[0][0]):
            result.append(index)
    return result[0:5]
