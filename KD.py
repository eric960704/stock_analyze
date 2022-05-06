import pandas as pd
import pymysql

MYSQL_HOST = 'localhost'
MYSQL_DB = 'stock'
MYSQL_USER = 'root'
MYSQL_PASS = ''

def connect_mysql():  # 連線資料庫
    global connect, cursor
    connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()
connect_mysql()

# 呼叫連線資料庫函式
stock = pd.read_sql('SELECT * FROM tech order by Id', con=connect)  # 使用connect指定的Mysql獲取資料
# stock = stock.set_index('Date')

# RSV值
def Rsv(stock_price):
    Rsv = (stock_price.Close - stock_price.Low.rolling(window=9).min()) / (stock_price.High.rolling(window=9).max() -
                                                                stock_price.Low.rolling(window=9).min()) * 100

    Rsv=pd.DataFrame(index=Rsv.index,data=Rsv.values,columns=['Rsv'])
    return (Rsv)

# K值
def K(stock_price, Rsv):
    K = []
    K_today = 0

    for i in range(8):
        K.append(0)

    for i in range(len(stock_price) - 8):
        K_today = K_today * 2 / 3 + Rsv[i + 8] * (1 / 3)
        K.append(K_today)

    return (K)

# D值
def D(stock_price, K):
    D = []
    D_today = 0

    for i in range(8):
        D.append(0)

    for i in range(len(stock_price) - 8):
        D_today = D_today * 2 / 3 + K[i + 8] * (1 / 3)
        D.append(D_today)
    return (D)

"""iloc"""
# K值
def K_iloc(stock_price, Rsv):
    K = []
    K_today = 0

    for i in range(8):
        K.append(0)

    for i in range(len(stock_price) - 8):
        K_today = K_today * 2 / 3 + Rsv.iloc[i + 8] * (1 / 3)
        K.append(K_today)

    return (K)

# D值
def D_iloc(stock_price, K):
    D = []
    D_today = 0

    for i in range(8):
        D.append(0)

    for i in range(len(stock_price) - 8):
        D_today = D_today * 2 / 3 + K.iloc[i + 8] * (1 / 3)
        D.append(D_today)
    return (D)
"""iloc"""

#KD 最佳化
#D_buy_min  D大於多少買下限
#D_buy_max  D大於多少買上限
#D_sell_min  D小於多少賣下限
#D_sell_max  D小於多少賣上限

def best_KD(stock_price, D_buy_min, D_buy_max, D_sell_min, D_sell_max, max_op, min_op):

    final_sumpal = -10000  # 假設損益初始值
    BH = stock_price.Open[-1] - stock_price.Open[0] #股票漲幅
    better_num = {"代碼": 0, "最佳損益": 0.0, "股票漲幅": 0.0, "最佳KD值買": 0, "最佳KD值賣": 0, "交易次數": 0,
                  "獲利次數": 0, "虧損次數": 0, "平均每次交易損益": 0.0, "平均每次交易勝率": 0.0, "單次最大獲利": 0.0,
                  "單次最大虧損": 0.0}
    stock_price = pd.merge(stock_price,Rsv(stock_price), left_index=True, right_index=True)
    stock_price['K'] = K(stock_price,stock_price['Rsv'])
    stock_price['D'] = K(stock_price,stock_price['K'])
    for buy in range(D_buy_min,D_buy_max+1,1):
        for sell in range(D_sell_max,D_sell_min-1,-1):
            sign = []  # 買賣訊號
            retain = []  # 留倉
            sumpal = []  # 策略累計損益
            pal = []  # 當前損益
            single_pal = []  # 單筆交易損益
            trade_count = 0  # 交易次數
            win_count = 0  # 獲利次數
            max_pal = 0  # 單次最大獲利
            min_pal = 0  # 單次最大虧損
            single_pal.append(0)
            sumpal.append(0)
            pal.append(0)
            retain.append(0)
            sign.append(0)

            for i in range(1, len(stock_price)):
                """交易訊號"""
                if stock_price.K[i] >= buy:
                    if stock_price.K[i-1] <= stock_price.D[i-1] and stock_price.K[i] > stock_price.D[i]:
                        sign.append(1)
                    else:
                        sign.append(0)
                elif stock_price.K[i] <= sell:
                    if stock_price.K[i-1] >= stock_price.D[i-1] and stock_price.K[i] < stock_price.D[i]:
                        sign.append(-1)
                    else:
                        sign.append(0)
                else:
                    sign.append(0)
                """交易訊號"""

                """留倉"""
                if retain[i - 1] >= 0 and sign[i - 1] == -1:
                    retain.append(-1)
                    if single_pal[trade_count] > 0:  # 獲勝次數
                        win_count = win_count + 1
                        if single_pal[trade_count] > max_pal:  # 最大單次獲利
                            max_pal = single_pal[trade_count]
                    elif single_pal[trade_count] < min_pal:  # 最大單次虧損
                        min_pal = single_pal[trade_count]
                    trade_count = trade_count + 1
                    single_pal.append(0)

                elif retain[i - 1] <= 0 and sign[i - 1] == 1:
                    retain.append(1)
                    if single_pal[trade_count] > 0:  # 獲勝次數
                        win_count = win_count + 1
                        if single_pal[trade_count] > max_pal:  # 最大單次獲利
                            max_pal = single_pal[trade_count]
                    elif single_pal[trade_count] < min_pal:  # 最大單次虧損
                        min_pal = single_pal[trade_count]
                    trade_count = trade_count + 1
                    single_pal.append(0)

                elif retain[i - 1] + sign[i - 1] >= max_op:
                    retain.append(max_op)
                elif retain[i - 1] + sign[i - 1] <= min_op:
                    retain.append(min_op)
                else:
                    retain.append(sign[i - 1] + retain[i - 1])
                """留倉"""

                """損益計算"""
                pal.append(
                    retain[i] * (stock_price.Close.values[i] - stock_price.Open.values[i]) +
                    retain[i - 1] * (stock_price.Open.values[i] - stock_price.Close.values[i - 1]))

                single_pal[trade_count] = single_pal[trade_count] + pal[i]  # 單次損益計算

                sumpal.append(sumpal[i - 1] + pal[i])
                """損益計算"""

            if (sumpal[-1] > final_sumpal): # 出現更好的損益
                final_sumpal = sumpal[-1]

                """檢查最後一次交易"""
                if (retain[-1] != 0):
                    if single_pal[trade_count] > 0:
                        win_count = win_count + 1
                        if single_pal[trade_count] > max_pal:  # 最大單次獲利
                            max_pal = single_pal[trade_count]
                    elif single_pal[trade_count] < min_pal:  # 最大單次虧損
                        min_pal = single_pal[trade_count]
                """檢查最後一次交易"""

                # 檢查有無交易
                if trade_count == 0:
                    better_num = None
                    break

                date_sign = pd.Series(retain, index=stock_price.index)  # 建立一個日期+買賣訊號的Series
                date_close = pd.Series(stock_price.Close, index=stock_price.index)  # 建立一個日期+收盤價的Series

                better_num.update({"代碼": stock_price.Id[0],
                                   "最佳損益": round(final_sumpal,2),
                                   "股票漲幅": round(BH,2),
                                   "最佳KD值買": buy,
                                   "最佳KD值賣": sell,
                                   "交易次數": trade_count,
                                   "獲利次數": win_count,
                                   "虧損次數": trade_count - win_count,
                                   "平均每次交易損益": round(final_sumpal / trade_count,2),
                                   "平均每次交易勝率": round(abs(win_count / trade_count) * 100,2),
                                   "單次最大獲利": round(max_pal,2),
                                   "單次最大虧損": round(min_pal,2),
                                   "損益變化": sumpal,
                                   "收盤價": date_close,
                                   "買賣訊號": date_sign,
                                   "日期區間": stock_price.index.date
                                   })
    return better_num


"""輸入代碼與日期回測"""
def simple_back_KD(id,MaxKDUp,MaxKDLower,MinKDUp,MinKDLower,StartDate,EndDate):#單一股票取得結果
    stock_price = stock.loc[(stock.Id == id)]
    if stock_price.empty:
        return None

    stock_price = stock_price.set_index('Date')
    stock_price.index = pd.to_datetime(stock_price.index)
    stock_price = stock_price.loc[(stock_price.index >= StartDate) & (stock_price.index <= EndDate)]
    stock_price = stock_price.sort_index()

    cmp = best_KD(stock_price,MaxKDUp,MaxKDLower,MinKDUp,MinKDLower,1,-1)

    return cmp
"""輸入代碼與日期回測"""


"""檢查訊號"""
def CheckKD(stock_id,D_Buy,D_Sell) :
    stock_price = stock.loc[(stock.Id == stock_id)]
    stock_price = stock_price.set_index('Date')
    stock_price = pd.merge(stock_price, Rsv(stock_price), left_index=True, right_index=True)
    stock_price['K'] = K_iloc(stock_price, stock_price['Rsv'])
    stock_price['D'] = K_iloc(stock_price, stock_price['K'])
    if stock_price.K.iloc[-1] >= D_Buy:
        if stock_price.K.iloc[-2] <= stock_price.D.iloc[-2] and stock_price.K.iloc[-1] > stock_price.D.iloc[-1]:
            return 1
        else:
            return 0
    elif stock_price.K.iloc[-1] <= D_Sell:
        if stock_price.K.iloc[-2] >= stock_price.D.iloc[-2] and stock_price.K.iloc[-1] < stock_price.D.iloc[-1]:
            return -1
        else:
            return 0
    else:
        return 0
"""檢查訊號"""