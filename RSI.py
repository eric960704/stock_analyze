import pandas as pd
import pymysql
import talib as tb

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
connect_mysql()

# 呼叫連線資料庫函式
stock = pd.read_sql('SELECT * FROM tech order by Date', con=connect)  # 使用connect指定的Mysql獲取資料


#max_op 部位上限
#min_op 部位下限
#ShortRSI_min RSI下限
#ShortRSI_max RSI上限
#LongRSI_min RSI下限
#LongRSI_max RSI上限

def best_RSI(stock_price,ShortRSI_min,ShortRSI_max,LongRSI_min,LongRSI_max,max_op,min_op):
    final_sumpal = -10000  # 假設損益初始值
    BH = stock_price.Open[-1] - stock_price.Open[0]  # 股票漲幅
    better_num = {"代碼": 0, "最佳損益": 0.0, "股票漲幅": 0.0, "最佳短RSI": 0,"最佳長RSI": 0,"交易次數": 0,"獲利次數": 0, "虧損次數": 0,
                  "平均每次交易損益": 0.0, "平均每次交易勝率": 0.0, "單次最大獲利": 0.0,"單次最大虧損": 0.0}

    for ShortRSI in range(ShortRSI_min, ShortRSI_max+1):
        for LongRSI in range(LongRSI_min, LongRSI_max + 1):

            stock_price['ShortRSI'] = tb.RSI(stock_price['Close'].to_numpy(), timeperiod=ShortRSI)
            stock_price['LongRSI'] = tb.RSI(stock_price['Close'].to_numpy(), timeperiod=LongRSI)

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

            for i in range(1,len(stock_price)):
                """交易訊號"""
                if stock_price.LongRSI[i] >= 50 :
                    if stock_price.ShortRSI[i-1] <= stock_price.LongRSI[i-1] and stock_price.ShortRSI[i] > stock_price.LongRSI[i] :
                        sign.append(1)
                    else:
                        sign.append(0)
                elif stock_price.LongRSI[i] < 50 :
                    if stock_price.ShortRSI[i-1] >= stock_price.LongRSI[i-1] and stock_price.ShortRSI[i] < stock_price.LongRSI[i] :
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
                if(retain[-1] != 0):
                    if single_pal[trade_count] > 0 :
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
                                   "最佳短RSI": ShortRSI,
                                   "最佳長RSI": LongRSI,
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
def simple_back_RSI(id,RsiLower1,RsiLower2,RsiUper1,RsiUper2,StartDate,EndDate):#單一股票取得結果
    stock_price = stock.loc[(stock.Id == id)]
    if stock_price.empty:
        return None

    stock_price = stock_price.set_index('Date')
    stock_price.index = pd.to_datetime(stock_price.index)
    stock_price = stock_price.loc[(stock_price.index >= StartDate) & (stock_price.index <= EndDate)]
    stock_price = stock_price.sort_index()

    cmp = best_RSI(stock_price,RsiLower1,RsiLower2,RsiUper1,RsiUper2,1,-1)

    return cmp
"""輸入代碼與日期回測"""

"""檢查訊號"""
def CheckRSI(stock_id,ShortRSI,LongRSI) :
    stock_price = stock.loc[(stock.Id == stock_id)]
    stock_price = stock_price.set_index('Date')
    stock_price['ShortRSI'] = tb.RSI(stock_price.loc[:,"Close"].to_numpy(), timeperiod=ShortRSI)
    stock_price['LongRSI'] = tb.RSI(stock_price.loc[:,"Close"].to_numpy(), timeperiod=LongRSI)

    if stock_price.LongRSI.iloc[-1] >= 50:
        if stock_price.ShortRSI.iloc[-2] <= stock_price.LongRSI.iloc[-2] and stock_price.ShortRSI.iloc[-1] > stock_price.LongRSI.iloc[
            -1]:
            return 1
        else:
            return 0
    elif stock_price.LongRSI.iloc[-1] < 50:
        if stock_price.ShortRSI.iloc[-2] >= stock_price.LongRSI.iloc[-2] and stock_price.ShortRSI.iloc[-1] < stock_price.LongRSI.iloc[
            -1]:
            return -1
        else:
            return 0
    else:
        return 0
"""檢查訊號"""