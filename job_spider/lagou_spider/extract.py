#!/usr/bin/env python

#解析网页类

from bs4 import BeautifulSoup as bp
import re
import sqlite3
import threading


class lagou_extract():
    def __init__(self):
        pass
    def start_1(self,text):
        s = bp(text,'html.parser')
        e = s.find_all('a',class_='position_link')
        a = []
        for x in e:
            a.append('http:'+x.get('href'))
        return a
    def start_2(self,text):
        s = bp(text,'html.parser')
        e = s.find('dd', class_='job_request')
        fromsite = '拉勾网'
        #
        positionType = s.find('li',class_='labels').string
        salary = s.find('span',class_='salary').string
        positionName = s.find('span',class_='ceil-job').string
        #
        c = ''
        for x in e.find_all('span'):
            c = c+x.string
        d = c.split('/')
        #
                            city = d[1]                                 copyright()
        workYear = d[2]
        company = s.find('div',class_='company').string
        #
        u = s.find('dd',class_='job_bt')
        jobDes = ''
        for j in u.strings:
            jobDes = jobDes+j
        #
        n = s.find('ul',class_='c_feature')
        p = n.get_text()
        p = p.replace(' ','')
        p = p.strip()
        p = p.split()
        #
        industryField = p[0]
        companySize = p[4]
        financeStage = p[2]
        #
        rate = ''
        number = ''
        #
        conn = sqlite3.connect('lagou.db')
        cursor = conn.cursor()
        sql = 'insert into lagou values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        try:
            cursor.execute(sql,(fromsite,positionType,positionName,salary,education,city,workYear,jobDes,company,companySize,financeStage,industryField,rate,number))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()




#
#
# class zhilian_extract():
#     def __init__(self):
#         pass
#     def start(self,text,positionType):
#         s = bp(text,'html.parser')
#         a = s.find_all('table')
#         a.pop(0)
#         #
#         positionType = positionType
#         #
#         for b in a:
#             positionName = b.a.get_text()
#             salary = b.find('td',class_='zwyx').get_text()
#             city = b.find('td',class_='gzdd').get_text()
#             #
#             c = b.ul.find_all('span')
#             financeStage = c[1].string.split('：')[1]
#             companySize = c[2].string.split('：')[1]
#             d = c[3].string.split('：')[0]
#             if d == '学历':
#                 education = c[3].string.split('：')[1]
#                 workYear = '不限'
#             else:
#                 if d == '经验':
#                     workYear = c[3].string.split('：')[1]
#                 else:
#                     education = c[4].string.split('：')[1]
#             industryField = '计算机软件'
#             jobDes = b.find('li',class_='newlist_deatil_last')
#             #
#             conn = sqlite3.connect('xxx.db')
#             cursor = conn.cursor()
#             sql = 'insert into xxx values(?,?,?,?,?,?,?,?,?,?)'
#             cursor.execute(sql, (positionType, positionName, salary, education, city, workYear, jobDes, company, companySize, financeStage,industryField,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#
#
#
#
# class qiancheng_extract():
#     def __init__(self):
#         pass
#     def start1(self,text,positionType):
#         s = bp(text,'html.parser')
#         a = s.find_all('div',class_='el')
#         b = []
#         for x in range(11):
#             a.pop(0)
#         for y in a:
#             b.append(y.a.get('href'))
#         return b
#     def start2(self,text,positionType):
#         s = bp(text,'html.parser')
#         positionName = s.find('div',class_='tHeader').h1.get_text()
#         company = s.find('div',class_='tHeader').a.get_text()
#         #
#         a = s.find('div',class_='tHeader').find('p',class_='msg').get_text()
#         a.strip()
#         a = a.split()
#         #
#         financeStage = a[0]
#         companySize = a[2]
#         industryField = a[4]
#         city = s.find('span',class_='lname').string
#         salary = s.find('div',class_='cn').strong.string
#         jobDes = s.find('div',class_='bmsg').get_text()
#         #
#         b = s.find('duv',class_='t1').get_text()
#         b = b.split()
#         if '经验' in b[0]:
#             workYear = b[0]
#             education = b[1]
#         else:
#             workYear = False
#             education = b[0]
#             #
#         conn = sqlite3.connect('xxx.db')
#         cursor = conn.cursor()
#         sql = 'insert into xxx values(?,?,?,?,?,?,?,?,?,?)'
#         cursor.execute(sql, (positionType, positionName, salary, education, city, workYear, jobDes, company, companySize, financeStage,industryField,))
#         conn.commit()
#         cursor.close()
#         conn.close()
