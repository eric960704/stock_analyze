import csv
import MA
import KD
import RSI
import bolling
import MACD

total = {}

# 開啟 CSV 檔案
with open('buyform.csv', newline='') as csvfile:
  rows = csv.reader(csvfile)

  for row in rows:
    if row[5] == "MA":
      sign = MA.CheckMA(int(row[0]),int(row[1]),int(row[2]))
      if sign == 1:
        total[row[0]] = 1
      elif sign == -1:
        total[row[0]] = -1

    elif row[5] == "KD":
      sign = KD.CheckKD(int(row[0]),int(row[1]),int(row[2]))
      if sign == 1:
        total[row[0]] = 1
      elif sign == -1:
        total[row[0]] = -1

    elif row[5] == "RSI":
      sign = RSI.CheckRSI(int(row[0]),int(row[1]),int(row[2]))
      if sign == 1:
        total[row[0]] = 1
      elif sign == -1:
        total[row[0]] = -1

    elif row[5] == "BB":
      sign = bolling.CheckBB(int(row[0]),int(row[1]))
      if sign == 1:
        total[row[0]] = 1
      elif sign == -1:
        total[row[0]] = -1

    elif row[5] == "MACD":
      sign = MACD.CheckMACD(int(row[0]),int(row[1]),int(row[2]))
      if sign == 1:
        total[row[0]] = 1
      elif sign == -1:
        total[row[0]] = -1

# for item in total.items():
#   print(item)

