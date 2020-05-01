import json
import sqlite3 
# 匯入 json 台灣電力公司資料
fn = '台灣電力公司_各縣市住宅、服務業及機關用電統計資料.json'
with open(fn,'r',encoding = 'utf-8') as file:
    jsdata = json.load(file)
for i in range(2277):
    list_js = jsdata[i]
    list_js["縣市用電佔比"] = list_js.pop("縣市用電佔比(%)")
    list_js["住宅部門售電量"] = list_js.pop("住宅部門售電量(度)")
    list_js["住宅部門用電佔比"] = list_js.pop("住宅部門用電佔比(%)")
    list_js["合計售電量"] = list_js.pop("合計售電量(度)")
    list_js["服務業部門售電量"] = list_js.pop("服務業部門售電量(度)")
    list_js["服務業部門用電佔比"] = list_js.pop("服務業部門用電佔比(%)")
    list_js["機關用電售電量"] = list_js.pop("機關用電售電量(度)")
    list_js["機關用電用電佔比"] = list_js.pop("機關用電用電佔比(%)")
    list_js["農林漁牧售電量"] = list_js.pop("農林漁牧售電量(度)")
    list_js["農林漁牧用電佔比"] = list_js.pop("農林漁牧用電佔比(%)")
# 將 json 台灣電力公司匯入sqlite
# 連接 electric.sqlite 資料庫
conn = sqlite3.connect('people_eletrice.sqlite')

# 建立 cursor 物件
cursor = conn.cursor()

# 建立一個資料表
sqlstr = '''CREATE TABLE IF NOT EXISTS eletrice 
    ("住宅部門售電量" TEXT, 
    "住宅部門用電佔比" TEXT, 
    "合計售電量" TEXT, 
    "日期" TEXT, 
    "服務業部門售電量" TEXT, 
    "服務業部門用電佔比" TEXT, 
    "機關用電售電量" TEXT,
    "機關用電用電佔比" TEXT,
    "縣市" TEXT,
    "縣市用電佔比" TEXT,
    "農林漁牧售電量" TEXT,
    "農林漁牧用電佔比" TEXT);
'''
cursor.execute(sqlstr)


# 新增json資料
sqljson = '''
INSERT INTO eletrice 
(住宅部門售電量,
住宅部門用電佔比,
合計售電量,
日期,
服務業部門售電量,
服務業部門用電佔比,
機關用電售電量,
機關用電用電佔比,
縣市,
縣市用電佔比,
農林漁牧售電量,
農林漁牧用電佔比)
 VALUES ("{}","{}","{}","{}",
 "{}","{}","{}","{}","{}","{}","{}","{}");
 '''
 
for i in range(2277):
    list_js = jsdata[i]
    sql = sqljson.format(list_js['住宅部門售電量'],list_js['住宅部門用電佔比'],list_js['合計售電量'],list_js['日期'],list_js['服務業部門售電量'],list_js['服務業部門用電佔比'],list_js['機關用電售電量'],list_js['機關用電用電佔比'],list_js['縣市'],list_js['縣市用電佔比'],list_js['農林漁牧售電量'],list_js['農林漁牧用電佔比'])
    print(sql)
    cursor.execute(sql)
    # 更新
    conn.commit()
# 關閉資料庫連結
conn.close()