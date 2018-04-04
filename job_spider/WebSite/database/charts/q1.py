#!/usr/bin/env python

# 1.互联网中哪个招聘职位（技术）最高薪？

import sqlite3
import json


job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]

dbname = ['lagou1.db','zhilian1.db','51job1.db']

result = {'java':[],'python':[],'php':[],'c':[],'_net':[],'csharp':[],'cplusplus':[],'vb':[],'delphi':[], 'perl':[],'ruby':[],'hadoop':[],'node_js':[],'go':[],'asp':[], 'shujuwajue':[],'ziranyuyanchuli':[],'html5':[],'android':[],'ios':[],'wp':[], 'web前端':[],'flash':[],'javaScript':[],'u3d':[],'cocos2d_x':[] }


for x in dbname:
    conn = sqlite3.connect('经过薪资和职位描述处理后的数据/'+x)
    cursor = conn.cursor()
    for i in job:
        sql = 'select rowid,positionType,salary from'+' '+i
        a = cursor.execute(sql)
        b = a.fetchall()
        c = len(b)
        for y in range(c):
            money1 = b[y][2]
            money2 = money1.split('-')
            if len(money2) ==2:
                try:
                    money3 = int(money2[0])
                    money4 = int(money2[1])
                    money_result = int((money3+money4)/2)
                    result[i].append(money_result)
                except:
                    continue
            else:
                continue
            print('计算中.....')
    cursor.close()
    conn.close()


result2 = {'java':'','python':'','php':'','c':'','_net':'','csharp':'','cplusplus':'','vb':'','delphi':'', 'perl':'','ruby':'','hadoop':'','node_js':'','go':'','asp':'', 'shujuwajue':'','ziranyuyanchuli':'','html5':'','android':'','ios':'','wp':'', 'web前端':'','flash':'','javaScript':'','u3d':'','cocos2d_x':'' }

#计算各个职位的平均工资
def gongzi(r):
    for x in r:
        z = r[x]    #某个职位的所有工资集合
        p = 0
        for i in z:
            p = p + i

        pingjun = int(p/len(z))
        result2[x] = pingjun

    print(result2)
    print('共分析职位种类：')
    print(len(result2))
    result3 = json.dumps(result2,ensure_ascii=False)
    with open('q1.json','w') as f:
        f.write(result3)
    print('已经写入json')


gongzi(result)