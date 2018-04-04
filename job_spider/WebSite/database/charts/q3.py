#!/usr/bin/env python

#3.互联网哪个岗位需求量最大？百分比

import sqlite3
import json

job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]


job1 = {'java':0,'python':0,'php':0,'c':0,'_net':0,'csharp':0,'cplusplus':0,'vb':0,'delphi':0, 'perl':0,'ruby':0,'hadoop':0,'node_js':0,'go':0,'asp':0, 'shujuwajue':0,'ziranyuyanchuli':0,'html5':0,'android':0,'ios':0,'wp':0, 'web前端':0,'flash':0,'javaScript':0,'u3d':0,'cocos2d_x':0}
job2 = {'总计':0}
#百分比
job3 =  {'java':0,'python':0,'php':0,'c':0,'_net':0,'csharp':0,'cplusplus':0,'vb':0,'delphi':0, 'perl':0,'ruby':0,'hadoop':0,'node_js':0,'go':0,'asp':0, 'shujuwajue':0,'ziranyuyanchuli':0,'html5':0,'android':0,'ios':0,'wp':0, 'web前端':0,'flash':0,'javaScript':0,'u3d':0,'cocos2d_x':0}

dbname = ['lagou1.db','zhilian1.db','51job1.db']


for x in dbname:
    conn = sqlite3.connect('经过薪资和职位描述处理后的数据/'+x)
    cursor = conn.cursor()
    for y in job:
        sql = 'select count(*) from'+' '+y
        a = cursor.execute(sql)
        b = a.fetchall()
        s = b[0][0]
        job1[y] = job1[y] + s
        job2['总计'] = job2['总计']+s

print(job1)

def result(r):
    for z in r :
        a = r[z]
        print(a)
        print(job2['总计'])
        baifen = (a/job2['总计'])*100
        baifen2 = '%.2f'%baifen
        job3[z] = str(baifen2)+'%'

    with open('q3.json','w') as f:
        f.write(json.dumps(job3,ensure_ascii=False))
    print('写入json')
    cursor.close()
    conn.close()
result(job1)