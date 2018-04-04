#!/usr/bin/env python
#coding:utf8

import scrapy
from ..items import ItDataItem
from bs4 import BeautifulSoup as bp


job = ['Java','Python','PHP','C','.NET','C#','C++','VB','Delphi','Perl','Ruby','Hadoop','Node.js','Go','ASP','数据挖掘','自然语言处理','HTML5','Android','iOS','WP','web前端','Flash','JavaScript','U3D','COCOS2D-X',]
url_base = 'http://search.51job.com/jobsearch/search_result.php'

playload = {'keyword':'','curr_page':''}


class qiancheng(scrapy.Spider):

    name = 'zhilian'


    def start_requests(self):
        for p in range(1,1000):
            for j in job:
                playload['keyword'] = j
                playload['curr_page'] = p
                yield scrapy.Request(url_base,meta=playload,callback=self.parse)


    def parse(self, response):
        s = bp(response.body,'html_parser')
        a = s.find_all('div',class_='el')[10:]
        for x in a:
            link = x.a.get('href')
            yield scrapy.Request(link,callback=self.parse_detail)


    def parse_detail(self,response):
        s = bp(response.body,'html.parser')
        item = ItDataItem()
        a = s.find_all('div',class_='tHeader')[0]
        item['fromsite'] = '前程无忧'.encode('utf8')
        item['positionType'] = 0
        item['positionName'] = a.h1.get_text().encode('utf8')
        item['salary'] = a.strong.get_text().encode('utf8')
        item['city'] = a.span.get_text().encode('utf8')
        try:
            item['education'] = s.find_all('span',class_='sp2')[0].get_text()
            item['workYear'] = s.find_all('span',class_='sp1')[0].get_text()
        except:
            item['education'] = ''
            item['workYear'] = ''
        item['jobDes'] = a.find_all('div',class_='bmsg')[0].get_text().encode('utf8')
        item['company'] = a.find_all('p',class_='cname')[0].get_text().encode('utf8')
        item['companySize'] = a.find_all('p',class_='msg')[0].get_text().split('|')[1]
        item['financeStage'] = a.find_all('p',class_='msg')[0].get_text().split('|')[0]
        item['industryField'] = a.find_all('p',class_='msg')[0].get_text().split('|')[2]
        #-----#
        item['rate'] = ''
        item['number'] = ''
        yield item