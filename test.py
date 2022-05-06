import KD
import RSI
import pandas as pd
import pymysql
import matplotlib.pyplot as plt

MYSQL_HOST = 'localhost'
MYSQL_DB = 'stock'
MYSQL_USER = 'root'
MYSQL_PASS = ''

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def connect_mysql():  # 連線資料庫
    global connect, cursor
    connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()
connect_mysql()

# 呼叫連線資料庫函式
stock = pd.read_sql('SELECT * FROM tech order by Id', con=connect)  # 使用connect指定的Mysql獲取資料
stock = stock.set_index('Date')


stock_price = stock.loc[(stock.Id == 2357)]
# stock_price.index = pd.to_datetime(stock_price.index)
stock_price = stock_price.sort_index()
print(stock_price)


