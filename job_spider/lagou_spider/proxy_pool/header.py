#!/usr/bin/env python
#coding:utf8
import random


class header():
    def __init__(self):
        self.UA = ['Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
              'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)',
              'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)',
              ]

        self.Accept_language = 'zh-CN,zh;q=0.8'

        self.Accept_encoding = 'gzip'

        self.Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

       


    def headers(self):  # n为主函数调用伪造头时传来的随机值，用来随机选取首部
        headers_result = {
            'Accept': self.Accept,
            'Accept-Encoding': self.Accept_encoding,
            'Accept-Language': self.Accept_language,
            'User-Agent': random.choice(self.UA),
            'Connection': 'Keep-alive',
            'Cache-Control': 'max-age=0',

        }
        return headers_result
