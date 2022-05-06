import numpy as np
import matplotlib.pyplot as plt
import MA
import pymysql
import pandas as pd

MYSQL_HOST = 'localhost'
MYSQL_DB = 'stock'
MYSQL_USER = 'root'
MYSQL_PASS = ''

# 連線資料庫
def connect_mysql():
    global connect, cursor
    connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()

connect_mysql() # 呼叫連線資料庫函式
stock = pd.read_sql('SELECT * FROM tech order by Date', con=connect)  # 使用connect指定的Mysql獲取資料

stock_price = stock.loc[(stock.Id == 2317)]
stock_price = stock_price.set_index('Date')


result = MA.best_MA(stock_price,5,5,10,10,1,-1)

for i in range(len(result["買賣訊號"])):
    print(i)

# plt.plot(result["收盤價"])
#
#
# # 繪製一個黑色，兩端縮排的箭頭
# # ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
# #             xycoords='data',
# #             arrowprops=dict(facecolor='black', shrink=0.05)
# #             )
#
# plt.show()


