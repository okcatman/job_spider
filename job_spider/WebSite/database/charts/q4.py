#!/usr/bin/env python

# 4.哪个领域的公司最缺人？

#说明：由于智联和前程无忧的领域实在是很难细分，所以这里只分析拉勾网的数据

import sqlite3
import json


#领域分类：移动互联网、电子商务、O2O、数据服务、信息安全、企业服务、游戏、硬件、金融、教育、旅游、广告、医疗

job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]


field = {'移动互联网':0,'电子商务':0,'O2O':0,'数据服务':0,'信息安全':0,'企业服务':0,'游戏':0,'硬件':0,'金融':0,'教育':0,'旅游':0,'广告':0,'医疗':0}

field_zong = {'总计':0}

conn = sqlite3.connect('经过薪资和职位描述处理后的数据/lagou1.db')
cursor = conn.cursor()



for x in job:
    sql = 'select industryField from'+' '+x
    a = cursor.execute(sql)
    b = a.fetchall()
    for y in b:
        z = y[0]
        if '移动互联网' in z:
            field['移动互联网'] = field['移动互联网'] + 1
            field_zong['总计'] = field_zong['总计']+1
        if '电子商务' in z:
            field['电子商务'] = field['电子商务'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if 'O2O' in z :
            field['O2O'] = field['O2O'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '数据服务' in z:
            field['数据服务'] = field['数据服务'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '信息安全' in z:
            field['信息安全'] = field['信息安全'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '企业服务' in z:
            field['企业服务'] = field['企业服务'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '游戏' in z:
            field['游戏'] = field['游戏'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '硬件' in z:
            field['硬件'] = field['硬件'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '金融' in z:
            field['金融'] = field['金融'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '教育' in z:
            field['教育'] = field['教育'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '旅游' in z:
            field['旅游'] = field['旅游'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '广告' in z:
            field['广告'] = field['广告'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        if '医疗' in z:
            field['医疗'] = field['医疗'] + 1
            field_zong['总计'] = field_zong['总计'] + 1
        else:continue

cursor.close()
conn.close()
print(field)

field3 = {'移动互联网':'','电子商务':'','O2O':'','数据服务':'','信息安全':'','企业服务':'','游戏':'','硬件':'','金融':'','教育':'','旅游':'','广告':'','医疗':''}

def save(r):
    for t in r:
        z = r[t]
        bai = (z/field_zong['总计'])*100
        fen = '%.2f'%bai
        baifen = str(fen)+'%'
        field3[t] = baifen
    print(field3)
    with open('q4.json','w') as f:
        f.write(json.dumps(field3,ensure_ascii=False))
    print('写入json')

save(field)








