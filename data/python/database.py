import urllib
import pymysql
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

"""
DB 연결을 위한 변수
cursor는 연결된 객체(SQL 실행을 위한 객체)
"""
conn = pymysql.connect(host='j4a301.p.ssafy.io', port=3306, user='root', passwd='j301##', db='ssafy',
                       charset='utf8')
cursor = conn.cursor()


def read_api(res):
    """
    openApi를 받기 위한 url 및 서비스키
    """
    xmlUrl = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'

    apiKey = unquote(
        '1J7amwxnHZ22NEowHAjGL9ihrCj%2FI%2BTvgjIesAJH%2F81p%2FJ0hI2qmYcKjcOrEfPkA0wXoVVgrzJHz4i1%2BRRxv6A%3D%3D')
    """
    2019/1/1 ~ 현재까지의 데이터를 받기 위한 list 생성
    """
    df_list = pd.date_range(start='20190101', end='20190201').strftime("%Y%m%d").tolist()
    """
    중간에 끊기 insert문을 연결하기 위한 if문 추후 삭제할 예정
    """
    if res[0] < 9:
        return
    """
    날자별로 데이터를 받아오기 위한 반복문
    """
    for i in df_list:
        """
        openApi url과 함께 보낼 쿼리들을 urllib를 통해 생성
        """
        queryParams = '?' + urlencode(
            {
                quote_plus('ServiceKey'): apiKey,
                quote_plus('numOfRows'): '500',
                quote_plus('pageNo'): '1',
                quote_plus('examin_de'): i,
                quote_plus('prdlst_cd'): res[2]
            }
        )
        """
        openApi 호출 후 데이터 받기
        """
        response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

        """
        openApi 중 item만 받아오기
        """
        rows = xmlobj.findAll('item')
        
        """
        데이터가 없을 경우 다음 날짜로 이동
        """
        if not rows:
            continue
        
        """
        첫번째 row는 각 태그명이 들어있음
        """
        columns = rows[0].find_all()
        rowList = []
        nameList = []
        columnList = []

        """
        열만큼 반복해서 rowList에 저장
        """
        rowsLen = len(rows)
        for i in range(0, rowsLen):
            columns = rows[i].find_all()
            columnsLen = len(columns)
            for j in range(0, columnsLen):

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
        if res[3] is not None:
            result = result[result['prdlst_detail_cd'] == res[4]]
            if len(result.index) == 0:
                return
            
        """
        필요없는 행을 제거
        """
        result.drop(
            ['examin_area_cd', 'examin_mrkt_nm', 'examin_mrkt_cd', 'prdlst_nm', 'prdlst_cd', 'prdlst_detail_nm',
             'distb_step_se', 'distb_step', 'grad_cd', 'bfrt_examin_amt', 'prdlst_detail_cd', 'grad'],
            axis=1, inplace=True)
            
        """
        데이터를 DB에 저장
        """
        for index, data in result.iterrows():
            sql = "insert into ingredient_info(ingredient_id, ingredient_info_date, ingredient_info_price, ingredient_info_area, ingredient_info_unit) values(%s, %s, %s, %s, %s)"
            val = (res[0], data['examin_de'], data['examin_amt'], data['examin_area_nm'], data['stndrd'])
            cursor.execute(sql, val)

        """
        한번에 commit, 만약에 저장할 때 중간에 에러가 발생한다면, 전부 rollback
        """
        conn.commit()



def naver_api(name):
    
    """
    네이버 Api 연동을 위한 id, secret
    encText을 사용하여 name으로 검색
    """
    client_id = "bYj15csqOZPThddA4ZSW"
    client_secret = "n0KSJICGeo"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText + "&display=10&start=1&sort=sim"
    result = requests.get(url=url, headers={"X-Naver-Client-Id": client_id,
                                            "X-Naver-Client-Secret": client_secret})
                                            
    """
    받아온 데이터를 데이터프레임으로 변경
    필요없는 행 제거
    title에 검색한 이름은 태그가 붙어있어서 태그 제거
    """
    data = pd.DataFrame(result.json()["items"])
    data.drop(
        ['category1', 'category2', 'category3', 'category4', 'image', 'hprice', 'productId', 'productType', 'maker',
         'brand'], axis=1, inplace=True
    )
    data['title'] = data['title'].str.replace("</b>", "")
    data['title'] = data['title'].str.replace("<b>", "")
    print(data)


def main():
    
    """
    재료 데이터 DB에서 받아옴
    """
    sql = 'SELECT * FROM ingredient'
    cursor.execute(sql)

    result = cursor.fetchall()

    """
    재료들 하나하나 api 호출
    """
    for res in result:
        print(res[1])
        read_api(res)
        #naver_api(res[1])

    """
    DB연결 끊기
    """
    conn.close()


if __name__ == "__main__":
    main()
