#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bp
import time
# import re
# import random
from req_header import *
# from threading import Thread
import sqlite3

#拉勾网站类,拉勾是有抓取频率监控的，同一个ip的访问频率和访问次数不能过多

class lagou():
    def __init__(self,page,job):
        self.url_base='http://www.lagou.com/zhaopin/'
        self.job=job
        self.page = page
        self.url = self.url_base+self.job+'/'+str(self.page)
    def start_1(self):
        try:
            r = requests.get(self.url,headers=header().headers(),timeout=3)
            if r.status_code == 200:
                if '近期我们监控到您所用的IP地址出现异常' in r.text:
                    conn = sqlite3.connect('proxy.db')
                    cursor = conn.cursor()
                    sql = 'select * from proxy where rowid=?'
                    a = cursor.execute(sql,(random.randint(1,100),))
                    b = a.fetchall()
                    c = 'http://'+str(b[0][0])+':'+str(b[0][1])
                    cursor.close()
                    conn.close()
                    r = requests.get(self.url_base+self.job,headers=header().headers(),timeout=3)#proxies={'http':c})
                    return r.text
                else:
                    return r.text
            else:
                print('状态码不正常...........')
                print(r.status_code)
                print(self.url)
                # with open('log.txt','w')as f:
                #     f.write('拉勾网')
                #     f.write('状态码非200，职位：')
                #     f.write(self.job)
                #     f.write('职位页码：')
                #     f.write(self.page)
        except:
            return False
    def start_2(self,url):
        try:
            r = requests.get(url,headers=header().headers(),timeout=3)
            if r.status_code == 200:
                if '近期我们监控到您所用的IP地址出现异常' in r.text:
                    conn = sqlite3.connect('proxy.db')
                    cursor = conn.cursor()
                    sql = 'select * from proxy where rowid=?'
                    a = cursor.execute(sql, (random.randint(1, 100),))
                    b = a.fetchall()
                    cursor.close()
                    conn.close()
                    c = 'http://' + str(b[0][0]) + ':' + str(b[0][1])
                    r = requests.get(url, headers=header().headers(), timeout=3)#,proxies={'http': c})
                    return r.text
                else:
                    return r.text
            else:
                print('状态码不正常...........')
                print(r.status_code)
                print(url)
                # with open('log.txt', 'w')as f:
                #     f.write('拉勾网职位详情页')
                #     f.write('状态码非200')
                #     f.write('网址：')
                #     f.write(url)
        except:
            return False


#
#
# class zhilian():
#     def __init__(self,page,job):
#         self.page=page
#         self.url_base='http://sou.zhaopin.com/jobs/searchresult.ashx'
#         self.job=job
#         self.url_in = 160400
#         self.url_jl = '选择地区'
#     def satrt_1(self):
#         payload = {'in': self.url_in,'jl':self.url_jl,'kw':self.job,'p':self.page,}
#         r = requests.get(self.url_base,params=payload,headers=header(random.randint(0,8)).headers(),timeout=3)
#         if r.status_code == 200:
#             r.encoding = 'utf-8'
#             return r.text
#         else:
#             print('状态码不正常...........')
#             with open('log.txt', 'w')as f:
#                 f.write('智联招聘：')
#                 f.write('状态码非200，职位：')
#                 f.write(self.job)
#                 f.write('职位页码：')
#                 f.write(self.page)
#             return False
#     def start_2(self,url):
#         r = requests.get(url,headers=header(random.randint(0,8)).headers(),timeout=3)
#         if r.status_code==200:
#             r.encoding='utf-8'
#             return r.text
#         else:
#             print('状态码不正常...........')
#             with open('log.txt', 'w')as f:
#                 f.write('智联招聘职位详情页：')
#                 f.write('非200网址：')
#                 f.write(url)
#             return False
#
#
#
#
# class qiancheng():
#     def __init__(self,page,job):
#         self.url_base='http://search.51job.com/jobsearch/search_result.php'
#         self.page=page
#         self.job=job
#     def start_1(self):
#         payload = {'keyword':self.job,'curr_page':self.page}
#         r = requests.get(self.url_base,params=payload,timeout=3,headers=header(random.randint(0,8)).headers())
#         if r.status_code == 200:
#             r.encoding='GB2312'
#             return r.text
#         else:
#             print('状态码不正常...........')
#             with open('log.txt', 'w')as f:
#                 f.write('前程无忧：')
#                 f.write('状态码非200，职位：')
#                 f.write(self.job)
#                 f.write('职位页码：')
#                 f.write(self.page)
#             return False
#
#     def start_2(self,url):
#         r = requests.get(url,headers=header(random.randint(0,8)).headers(),timeout=3)
#         if r.status_code==200:
#             r.encoding='GB2312'
#             return r.text
#         else:
#             print('状态码不正常...........')
#             with open('log.txt', 'w')as f:
#                 f.write('前程无忧招聘职位详情页：')
#                 f.write('非200网址：')
#                 f.write(url)
#             return False
