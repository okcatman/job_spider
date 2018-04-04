	#!/usr/bin/env python

import sqlite3
import time

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
		salary = cursor.execute('select salary from'+' '+x+' where rowid='+str(id))
		salary_result = salary.fetchall()
		print(salary_result)
		salary_result_1 = salary_result[0][0]
		print(salary_result_1)
		salary_result_2 = salary_result_1.replace('/','') #将薪资中的k转换为具体数字
		salary_result_3 = salary_result_2.replace('月','')
		salary_result_4 = salary_result_3.replace('万','')
		salary_result_5 = salary_result_4.replace('+','')
		salary_result_6 = salary_result_5.replace('以','')
		salary_result_7 = salary_result_6.replace('年','')
		salary_result_9 = salary_result_7.replace('下','')
		print(salary_result_9)
		#salary_update = cursor.execute("update _net set salary=?"+str(salary_result_2)+" "+"where rowid="+str(id))
		salary_update = cursor.execute("update"+" "+x+" set salary=? where rowid=?",(str(salary_result_9),str(id)))

conn.commit()
cursor.close()
conn.close()

print('-----------------Over------------------')
	
	
