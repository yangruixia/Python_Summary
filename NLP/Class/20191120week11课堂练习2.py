#-*- coding:utf-8 -*-
import os
import re
import json
import sys
import pymysql

f = open('20191120week11练习1.txt', encoding = 'utf-8')
raw_text = f.read()
text = json.loads(raw_text)

# 连接数据库

conn = pymysql.connect('localhost','root','','kekenet')
cur = conn.cursor()
sql = 'set names utf8'
cur.execute(sql)


# 插入数据到数据库
for i in text:
    sql = "INSERT INTO `article` (`title`, `link`,`en`,`zh`) values (%s,%s,%s,%s)"
    title = i['title']
    link = i ['link']
    en = i ['en']
    zh = i ['zh']
    # 不能将list插入数据库中
    # content = i['content']
    # str(content)
    cur.execute(sql, [title, link, en, zh])
    conn.commit()
    # sql = 'select * from article'
    # cur.execute(sql)
    # data = cur.fetchall()
    # print(data)
cur.close()
conn.close()
f.close()
