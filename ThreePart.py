import pandas as pd
import pymysql
import MA
import  bolling
# MYSQL_HOST = '140.134.16.11'

MYSQL_HOST = 'localhost'
MYSQL_DB = 'stock'
# MYSQL_USER = 'test1'
MYSQL_USER = 'root'
MYSQL_PASS = ''

def connect_mysql():  # 連線資料庫
    global connect, cursor
    connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()
connect_mysql()

# 呼叫連線資料庫函式
stock = pd.read_sql('SELECT * FROM tech order by Date', con=connect)  # 使用connect指定的Mysql獲取資料
# stock = stock.set_index('Date')

stockid = sorted(set(stock.Id))
stock_Date = sorted(set(stock.Date))
train = []
train_day = int(len(stock_Date)*0.75)*99 #回測天數
test_day = int(len(stock_Date)*2/3)*99  #驗證天數

#回測
def Backtest(stock,train_day,codename):
    stock_price = stock.iloc[0:train_day, :]  #日期
    stock_price = stock_price.loc[(stock_price.Id == codename)]  #股票
    stock_price = stock_price.set_index('Date')
    tmp = bolling.best_BBands(20,20,40,40)['最佳損益']
    tmp = MA.best_MA(20, 20, 40, 40)
    tmp = bolling.best_BBands(20, 20, 40, 40)
    tmp = bolling.best_BBands(20, 20, 40, 40)
    tmp = bolling.best_BBands(20, 20, 40, 40)
    tmp['perday_profit'] = tmp["最佳損益"]/train_day
    return tmp

# df1=pd.DataFrame(train)
# df1.to_excel('1.xlsx')
# df2=pd.read_excel('1.xlsx')
test=[]

#驗證
def futuretest(stock,test_day,codename) :
    stock_test = stock.iloc[test_day:, :]  # 日期
    stock_price = stock_test.loc[(stock_test.Id == codename)]  # 股票
    stock_price = stock_price.set_index('Date')
    tmp = MA.best_MA(stock_price,train[0]["最佳短均線"],train[0]["最佳短均線"],train[0]["最佳長均線"],train[0]["最佳長均線"], 1, -1)
    tmp['預期獲利'] = round(train[0]['perday_profit']*test_day,2)
    return tmp


train.append(Backtest(stock,train_day,2330))
print(train)
test.append(futuretest(stock,test_day,2330))
print(test)

