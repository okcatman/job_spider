#!/usr/bin/env python
#coding:utf8
#抓取快代理代理ip

import requests
import time
import Queue
from bs4 import BeautifulSoup as bp
from header import *
from models import *
#import gevent
#from gevent import monkey
#print '切换异步'
#monkey.patch_all()
#print '切换完毕'



# ip_queue = Queue.Queue()     #存储Ip，列表对象，内部元素为字典{‘ip’：xxx，port：xxx}

def init_url():
    url = 'http://www.kuaidaili.com/free/inha/'
    urls = []
    for x in range(1,10):
        urls.append(url+str(x)+'/')
    print '抓取地址生成完毕'
    return urls

def get():
    urls = init_url()
    for x in urls:
        try:
            r = requests.get(x,headers=header().headers(),timeout=5)
            if r.status_code == 200:
		print '页面请求正常'
                status = extract(r.text)
                if status:
                    print '页面解析正常'
                else:
                    print 'ip在解析获取模块发生异常，继续前进...'
                    continue
        except:
            print ('connect error')
            continue

def extract(response):
    ip_port = {'ip':'','port':''}
    try:
        s = bp(response,'html.parser')
        a = s.find_all('tr')
        a.pop(0)
        for x in a:
            ip = x.find_all('td')[0].get_text()
            port = x.find_all('td')[1].get_text()
            ip_port['ip'] = ip
            ip_port['port'] = port
            if test_for_list(ip_port):
                if input('http://'+ip['ip']+':'+ip['port']):
                    print '插入成功'
                else:
                    print '插入失败'
                    continue
            else:
                print '验证失败'
                continue
        return True
    except:
        return False


def test_for_list(ip):            #ip获取后的测试函数，有效ip入库，无效ip抛弃
    try:
        r = requests.get('http://www.baidu.com',headers=header().headers(),timeout=5,proxies={'http':'http://'+ip['ip']+':'+ip['port']})
        if r.status_code == 200:
            print '有效ip'
            return True
        else:
            print '无效ip'+':'+ip['ip']+':'+ip['port']
            print 'http://'+ip['ip']+':'+ip['port']
            return False
    except:
        print '无效ip'
        return False

def test_for_queue(ip):          #对已进入队列的已验证ip进行再次检测，还有效就返回给调用对象，无效则继续请求下一个ip
    ip = ip_queue.get()
    try:
        r = requests.get('http://www.baidu.com',headers=header().headers(),timeout=5,proxies={'http':'http://'+ip['ip']+':'+ip['port']})
        if r.status_code == 200:
            return ip
        else:
            return False
    except:
        return False





def main():
    while True:
        get()
        time.sleep(180)



if __name__ == '__main__':
    main()

