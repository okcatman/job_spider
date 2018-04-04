#!/usr/bin/env python

import sqlite3

jobs = ['java','python','php','c','_net','csharp','cplusplus','vb','delphi', 'perl','ruby','hadoop','node_js','go','asp', 'shujuwajue','ziranyuyanchuli','html5','android','ios','wp', 'web前端','flash','javaScript','u3d','cocos2d_x', ]


conn = sqlite3.connect('51job1.db')

cursor = conn.cursor()


for x in jobs:

	row_id = cursor.execute('select rowid from'+' '+x)
	row_id2 = row_id.fetchall()

	print('总共'+str(len(list(row_id2)))+'条数据')
	print('即将进行职位：'+x)

	for row_id3 in row_id2:
		id = row_id3[0]
		print(id)
		jobdes = cursor.execute('select jobDes from'+' '+x+' where rowid='+str(id))
		jobdes_result = jobdes.fetchall()
		print(jobdes_result)
		jobdes_result_1 = jobdes_result[0][0]
		print(jobdes_result_1)
		jobdes_result_2 = jobdes_result_1.replace('\\n','') #将空格和换行符全部去掉
		jobdes_result_3 = jobdes_result_2.replace('\\xa0','')
		jobdes_result_4 = jobdes_result_3.replace('\\r','')
		jobdes_result_5 = jobdes_result_4.replace('\\t','')
		print(jobdes_result_5)
		#salary_update = cursor.execute("update _net set salary=?"+str(salary_result_2)+" "+"where rowid="+str(id))
		jobdes_update = cursor.execute("update"+" "+x+" set jobDes=? where rowid=?",(str(jobdes_result_5),str(id)))

conn.commit()
cursor.close()
conn.close()

print('-----------------Over------------------')
	
	
