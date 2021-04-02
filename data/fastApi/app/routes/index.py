from datetime import datetime
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db

router = APIRouter()


@router.get("/")
def index():
    return {"about": {
        "/": "about",
        "/open": "open API parsing"
    }}


@router.get('/open/{date}')
def openApi(date: str):
    xmlUrl = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'

    Api_key = unquote(
        '1J7amwxnHZ22NEowHAjGL9ihrCj%2FI%2BTvgjIesAJH%2F81p%2FJ0hI2qmYcKjcOrEfPkA0wXoVVgrzJHz4i1%2BRRxv6A%3D%3D')

    print(date)

    queryParams = '?' + urlencode(
        {
            quote_plus('ServiceKey'): Api_key,
            quote_plus('numOfRows'): '5000',
            quote_plus('pageNo'): '1',
            quote_plus('examin_de'): '20210311'
        }
    )

    response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

    rows = xmlobj.findAll('item')

    columns = rows[0].find_all()
    print(columns[0].text)
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
    result.drop(
        ['examin_area_cd', 'examin_mrkt_cd', 'prdlst_cd', 'distb_step_se', 'distb_step', 'prdlst_detail_cd', 'grad'],
        axis=1, inplace=True)
    js = result.to_json(orient='records')
    return js
