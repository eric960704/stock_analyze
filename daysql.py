import pymysql
import csv


MYSQL_HOST = 'localhost'
MYSQL_DB = 'stock'
MYSQL_USER = 'root'
MYSQL_PWD = ''


def connect_mysql():  # 連線資料庫
    global connect, cursor
    connect = pymysql.connect(host=MYSQL_HOST, db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PWD,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()


def DataToSql():
    connect_mysql()
    with open('price.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:  # 取出該月的每一天編號為stockno的股票資料
            print(item)
            # cursor.execute("DELETE FROM tech WHERE Date='2020/7/9';")
            cursor.execute("INSERT INTO tech VALUES(%s,%s,%s,%s,%s,%s)",
                           (str(item[0]), int(item[1]), float(item[2]), float(item[3]), float(item[4]), float(item[5])))  # 插入資料庫的SQL
            # 插入資料庫
            connect.commit()  # 插入時需要呼叫commit，才會修改資料庫
        cursor.close()
DataToSql()
