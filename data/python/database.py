import urllib
import pymysql
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

conn = pymysql.connect(host='j4a301.p.ssafy.io', port=3306, user='root', passwd='j301##', db='ssafy',
                       charset='utf8')
cursor = conn.cursor()


def read_api(res):
    xmlUrl = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'

    apiKey = unquote(
        '1J7amwxnHZ22NEowHAjGL9ihrCj%2FI%2BTvgjIesAJH%2F81p%2FJ0hI2qmYcKjcOrEfPkA0wXoVVgrzJHz4i1%2BRRxv6A%3D%3D')

    df_list = pd.date_range(start='20190101', end='20190201').strftime("%Y%m%d").tolist()
    if res[0] < 9:
        return
    for i in df_list:
        print(i)
        queryParams = '?' + urlencode(
            {
                quote_plus('ServiceKey'): apiKey,
                quote_plus('numOfRows'): '500',
                quote_plus('pageNo'): '1',
                quote_plus('examin_de'): i,
                quote_plus('prdlst_cd'): res[2]
            }
        )

        response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

        rows = xmlobj.findAll('item')
        if not rows:
            continue
        columns = rows[0].find_all()
        rowList = []
        nameList = []
        columnList = []

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

        result = pd.DataFrame(rowList, columns=nameList)
        if len(result[result['distb_step'] == '소비자가격'].index) > 0:
            result = result[result['distb_step'] == '소비자가격']
        q = result.loc[:, ['stndrd']]
        if res[3] is not None:
            result = result[result['prdlst_detail_cd'] == res[4]]
            if len(result.index) == 0:
                return
        result.drop(
            ['examin_area_cd', 'examin_mrkt_nm', 'examin_mrkt_cd', 'prdlst_nm', 'prdlst_cd', 'prdlst_detail_nm',
             'distb_step_se', 'distb_step', 'grad_cd', 'bfrt_examin_amt', 'prdlst_detail_cd', 'grad'],
            axis=1, inplace=True)

        for index, data in result.iterrows():
            sql = "insert into ingredient_info(ingredient_id, ingredient_info_date, ingredient_info_price, ingredient_info_area, ingredient_info_unit) values(%s, %s, %s, %s, %s)"
            val = (res[0], data['examin_de'], data['examin_amt'], data['examin_area_nm'], data['stndrd'])
            cursor.execute(sql, val)

        conn.commit()

        print(result)



def naver_api(name):
    client_id = "bYj15csqOZPThddA4ZSW"
    client_secret = "n0KSJICGeo"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText + "&display=10&start=1&sort=sim"
    result = requests.get(url=url, headers={"X-Naver-Client-Id": client_id,
                                            "X-Naver-Client-Secret": client_secret})
    # print(result.json()["items"])
    data = pd.DataFrame(result.json()["items"])
    data.drop(
        ['category1', 'category2', 'category3', 'category4', 'image', 'hprice', 'productId', 'productType', 'maker',
         'brand'], axis=1, inplace=True
    )
    data['title'] = data['title'].str.replace("</b>", "")
    data['title'] = data['title'].str.replace("<b>", "")
    print(data)


def main():
    sql = 'SELECT * FROM ingredient'
    cursor.execute(sql)

    result = cursor.fetchall()


    for res in result:
        print(res[1])
        read_api(res)
        #naver_api(res[1])

    conn.close()


if __name__ == "__main__":
    main()
