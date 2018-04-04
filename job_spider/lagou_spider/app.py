#!/usr/bin/env python
#coding:utf8
#一个全新的爬虫

import requests
import time
# from threading import Thread
from bs4 import BeautifulSoup as bp
# import re
from req_header import header
import random
import sqlite3
from spider import lagou   #,zhilian,qiancheng
from extract import lagou_extract     #,zhilian_extract,qiancheng_extract
from queue import Queue


def app():
    q_1 = Queue()
    job = ['Java','Python','PHP','C','.NET','C#','C++','VB','Delphi','Perl','Ruby','Hadoop','Node.js','Go','ASP','shujuwajue','ziranyuyanchuli','HTML5','Android','iOS','WP','webqianduan','Flash','JavaScript','U3D','COCOS2D-X',]
    page = 1
    for x in job:
        while page <= 30:
            r = lagou(page,x).start_1()
            if r:
                e = lagou_extract().start_1(r)
                for y in e:
                    q_1.put(y)
                if q_1.empty():
                    print('error queue1')
                    continue
                else:
                    for z in range(q_1.qsize()):
                        qq = q_1.get()
                        print(qq)
                        r = lagou(page,x).start_2(qq)
                        if r:
                            e = lagou_extract().start_2(r)
                            if e:
                                print('入库成功')
                            else:
                                print('入库失败')
                        else:
                            print('请求详细职位页面出错')
                page = page + 1
            else:
                continue
    # print('线程1完毕')


# def th_2():
#     job = ['Java','Python','PHP','C','.NET','C#','C++','VB','Delphi','Perl','Ruby','Hadoop','Node.js','Go','ASP','数据挖掘','自然语言处理','HTML5','Android','iOS','WP','web前端','Flash','JavaScript','U3D','COCOS2D-X',]
#     page = 1
#     for x in job:
#         while page <=2000:
#             r = zhilian(page,x).satrt_1()
#             e = zhilian_extract().start(r,x)
#             page = page+1
#     print('线程2执行完毕')
#
# def th_3():
#     q_3 = Queue()
#     job = ['Java', 'Python', 'PHP', 'C', '.NET', 'C#', 'C++', 'VB', 'Delphi', 'Perl', 'Ruby', 'Hadoop', 'Node.js', 'Go','ASP', '数据挖掘', '自然语言处理', 'HTML5', 'Android', 'iOS', 'WP', 'web前端', 'Flash', 'JavaScript', 'U3D','COCOS2D-X', ]
#     page = 1
#     for x in job:
#         while page<=2000:
#             r = qiancheng(page,x).start_1()
#             e = qiancheng_extract().start1(r,x)
#             for y in e:
#                 q_3.put(y)
#             if q_3.empty():
#                 print('error queue3')
#                 continue
#             else:
#                 for z in range(q_3.qsize()):
#                     r = qiancheng(page,x).start_2(q_3.get())
#             page = page + 1
#     print('线程3执行完毕')


def main():
    print('线程启动完毕开始爬取....')
    app()
    print('爬取结束')



if __name__ == '__main__':
    main()



