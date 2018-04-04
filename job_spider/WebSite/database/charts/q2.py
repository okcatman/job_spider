#!/usr/bin/env python

# 2.互联网哪种规模的公司最土豪？


# 说明：由于智联和前程无忧的数据里公司类型只分为民营、外资、股份制、上市公司这几类
#      而拉勾网分企业类型是分为初创上市融资未融资A轮B轮等所以本程序只分析拉勾网


import sqlite3
import json

dbname = '经过薪资和职位描述处理后的数据/lagou2.db'
job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]

conn = sqlite3.connect(dbname)
cursor = conn.cursor()

######
#初创型：Nomoney
#成长型：Noneed
#天使轮：Angel
#A轮：Astage
#B轮：Bstage
#C轮：Cstage
#D轮：Dstage
#上市：IPO
######

stage = {'初创型':[],'成长型':[],'天使轮':[],'A轮':[],'B轮':[],'C轮':[],'D轮':[],'上市':[]}


for x in job:
    sql = 'select salary,financeStage from'+' '+x
    a = cursor.execute(sql)
    b = a.fetchall()
    for y in b:
        m1 = y[0]
        s = y[1]
        m2 = m1.split('-')
        if len(m2) == 2:
            try:
                m3 = int((int(m2[0])+int(m2[1]))/2)
                if '天使轮' in s:
                    stage['天使轮'].append(m3)
                    continue
                if '初创型' in s:
                    stage['初创型'].append(m3)
                    continue
                if 'A轮' in s:
                    stage['A轮'].append(m3)
                    continue
                if 'B轮' in s:
                    stage['B轮'].append(m3)
                    continue
                if 'C轮' in s:
                    stage['C轮'].append(m3)
                    continue
                if 'D轮' in s:
                    stage['D轮'].append(m3)
                    continue
                if '上市' in s:
                    stage['上市'].append(m3)
                    continue
                if '成长型' in s:
                    stage['成长型'].append(m3)
                else:       continue
            except:continue
        else:
            continue
cursor.close()
conn.close()
print(stage)

stage2 = {'初创型':'','成长型':'','天使轮':'','A轮':'','B轮':'','C轮':'','D轮':'','上市':''}

def result(r):
    for z in r:
        e = r[z]
        ma = 0
        for s in e:
            ma = ma + s #薪资累加
        if len(e) != 0:
            pingjun = int(ma/len(e))
            stage2[z]=pingjun
        else:
            continue
    print(stage2)
    with open('q2.json','w') as f:
        f.write(json.dumps(stage2,ensure_ascii=False))
    print('写入json完毕')


#运行
result(stage)