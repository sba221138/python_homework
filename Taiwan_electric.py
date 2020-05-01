import json
import sqlite3 
# 匯入 json 台灣電力公司資料
fn = '台灣電力公司_各縣市住宅、服務業及機關用電統計資料.json'
with open(fn,'r',encoding = 'utf-8') as file:
    jsdata = json.load(file)
# 將 json 台灣電力公司匯入sqlite
# 連接 electric.sqlite 資料庫
conn = sqlite3.connect('people_eletrice.sqlite')

# 建立 cursor 物件
cursor = conn.cursor()

# 建立一個資料表
sqlstr = '''CREATE TABLE IF NOT EXISTS eletrice 
    ("住宅部門售電量(度)" TEXT, 
    "住宅部門用電佔比(%)" TEXT, 
    "合計售電量(度)" TEXT, 
    "日期" TEXT, 
    "服務業部門售電量(度)" TEXT, 
    "服務業部門用電佔比(%)" TEXT, 
    "機關用電售電量(度)" TEXT,
    "機關用電用電佔比(%)" TEXT,
    "縣市" TEXT,
    "縣市用電佔比(%)" TEXT,
    "農林漁牧售電量(度)" TEXT,
    "農林漁牧用電佔比(%)" TEXT)
'''
cursor.execute(sqlstr)

# 新增json資料
sqljson = '''
INSERT INTO eletrice 
(住宅部門售電量(度),
住宅部門用電佔比(%),
合計售電量(度),
日期,
服務業部門售電量(度),
服務業部門用電佔比(%),
機關用電售電量(度),
機關用電用電佔比(%),
縣市,
縣市用電佔比(%),
農林漁牧售電量(度),
'農林漁用電佔比(%)')
 VALUES ("{0}","{1}","{2}","{3}",
 "{4}","{5}","{6},"{7}","{8}","{9}","{10}","{11}")
 '''
 
for i in range(2277):
    data = jsdata[i]
    print(data)
    sql = sqljson.format(data['住宅部門售電量(度)'],data['住宅部門用電佔比(%)'],data['合計售電量(度)'],data['日期'],data['服務業部門售電量(度)'],data['服務業部門用電佔比(%)'],data['機關用電售電量(度)'],data['機關用電用電佔比(%)'],data['縣市'],data['縣市用電佔比(%)'],data['農林漁牧售電量(度)'],data['農林漁牧用電佔比(%)'])
    print(sql)
    cursor.execute(sql)


