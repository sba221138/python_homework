import csv
import sqlite3 

# 匯入 csv台灣人口資料 (民國101年 2012年)
fn2 = '101年3月行政區人口統計_縣市.csv'
with open(fn2,'r') as csvfile:
    csvdata = csv.reader(csvfile)
    list_csv = list(csvdata)

# 將 csv台灣人口匯入sqlite
# 連接people.sqlite 資料庫
conn = sqlite3.connect('people_eletrice.sqlite')

# 建立cursor物件
cursor = conn.cursor()

# 建立一個資料表
sqlstr = 'CREATE TABLE IF NOT EXISTS people101 \
    ("縣市代碼" TEXT, \
    "縣市名稱" TEXT, \
    "戶數" TEXT, \
    "人口數" TEXT, \
    "男性人口數" TEXT, \
    "女性人口數" TEXT, \
    "資料時間" TEXT)'
cursor.execute(sqlstr)

# 新增csv資料
sqlstrcsv = '''
INSERT INTO people101 
(縣市代碼,縣市名稱,戶數,人口數,男性人口數,女性人口數,資料時間)
 VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")
 '''
for k in range(2,24):
    list1 = list_csv[k]
    sql = sqlstrcsv.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6])
    print(sql)
    cursor.execute(sql)

conn.commit()
conn.close()

  