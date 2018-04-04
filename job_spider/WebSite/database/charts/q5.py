#!/usr/bin/env python

# 5.互联网招聘职位的地域分布情况

import sqlite3
import json

dis = {}

job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]

dbname = ['lagou1.db']#,'zhilian1.db','51job1.db']

for x in dbname:
    conn = sqlite3.connect('经过薪资和职位描述处理后的数据/'+x)
    cursor = conn.cursor()
    for y in job:
        sql = 'select city from'+' '+y
        a = cursor.execute(sql)
        b = a.fetchall()
        for z in b:
            try:
                dis[z[0]] = dis[z[0]]+1
            except:
                dis[z[0]] = 1
    cursor.close()
    conn.close()
print(dis)
with open('q5.json','w') as f:
    f.write(json.dumps(dis,ensure_ascii=False))
print('写入json')