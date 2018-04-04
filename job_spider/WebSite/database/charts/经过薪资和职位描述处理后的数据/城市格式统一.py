#!/usr/bin/env python


import sqlite3


dbname = ['zhilian1.db','51job1.db']

job = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]


for x in dbname:
    conn = sqlite3.connect('经过薪资和职位描述处理后的数据/'+x)
    cursor = conn.cursor()
    for y in job:
        sql = 'select rowid,city from'+' '+y
        a = cursor.execute(sql)
        b = a.fetchall()
        for z in b:
            i = z[1].split('-')
            n = z[0]
            print(i)
            if len(i) == 2:
                p = i[0]
                print(p)
                cursor.execute("update"+" "+y+" "+"set city=? where rowid=?",(str(p),str(n)))
            else:continue

    conn.commit()
    cursor.close()
    conn.close()

print('----------------over---------------')
