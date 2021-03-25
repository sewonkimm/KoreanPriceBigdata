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


def main():
    sql = 'SELECT count(*) FROM ingredient_info'
    cursor.execute(sql)

    result = cursor.fetchall()

    conn.close()


if __name__ == "__main__":
    main()
