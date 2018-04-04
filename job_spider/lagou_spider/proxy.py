#!/usr/bin/env python


#http代理获取和验证独立进程---快代理

import time
import  requests
import sqlite3
from bs4 import BeautifulSoup
import re

url1 = 'http://www.kuaidaili.com/free/inha/'

page = 1



def get():
    conn = sqlite3.connect('proxy.db')
    cursor = conn.cursor()
    while page<10:
        url2 = url1 + str(page) + '/'
        r = requests.get(url2)
        if r.status_code == 200:
            s = BeautifulSoup(r.text,'html.parser')
            z = s.find_all('tr')
            l = len(z)
            for x in range(1,l):
                ip = re.findall('<td data-title="IP">(.*)</td>',str(z[x]))
                po = re.findall('<td data-title="PORT">(.*)</td>',str(z[x]))
                a = cursor.execute('select rowid from proxy where ip='+ip[0])
                b = a.fetchall()
                if len(b) == 0:
                    sql = 'insert into proxy values(?,?)'
                    cursor.execute(sql,(ip[0],po[0]))
                    conn.commit()
                else:
                    continue
        page = page + 1
    cursor.close()
    conn.close()



#质量检验
def check():
    conn = sqlite3.connect('proxy.db')
    cursor = conn.cursor()
    sql = 'select * from proxy'
    a = cursor.execute(sql)
    b = a.fetchall()
    for x in b:
        proxies = 'http://'+x[0]+':'+x[1]
        r = requests.get('http://www.baidu.com',proxies=proxies,timeout=3)
        if r.status_code == 200:
            continue
        else:
            sql = 'delete * from proxy where ip='+x[0]
            cursor.execute(sql)
            conn.commit()
    cursor.close()
    conn.close()


def main():
    get()
    check()

while True:
    main()
    time.sleep(120)












