#!/usr/bin/env python
#coding:utf8

#智联招聘蜘蛛爬虫

import scrapy
from it_data.items import ItDataItem
from bs4 import BeautifulSoup as bp


job = ['Java','Python','PHP','C','.NET','C#','C++','VB','Delphi','Perl','Ruby','Hadoop','Node.js','Go','ASP','数据挖掘','自然语言处理','HTML5','Android','iOS','WP','web前端','Flash','JavaScript','U3D','COCOS2D-X',]
url_base = 'http://sou.zhaopin.com/jobs/searchresult.ashx'

# playload = {'in':160400,'jl':'选择地区','kw':'','p':'','sm':'0'}


class zhilian(scrapy.Spider):

    name = 'zhilian'


    def start_requests(self):
        for p in range(1,1000):
            for j in job:
                url = url_base+'?'+'in=160400&'+'jl=选择地区&'+'sm=0&'+'kw='+j+'&'+'p='+str(p)
                yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):
        item = ItDataItem()
        s = bp(response.body,'html.parser')
        a = s.find_all('table',class_='newlist')
        a.pop(0)
        print a
        for x in a:
            item['fromsite'] = '智联招聘'
            item['positionType'] = x.b.get_text().encode('utf8')
            item['positionName'] = x.a.get_text().encode('utf8')
            item['salary'] = x.find_all('td',class_='zwyx')[0].get_text().encode('utf8')
            item['city'] = x.find_all('td', class_='gzdd')[0].get_text().encode('utf8')
            if  u'学历' in x.li.find_all('span')[3].get_text():
                item['education'] = x.li.find_all('span')[3].get_text().encode('utf8')
                item['workYear'] = ''
            else:
                if u'经验' in x.li.find_all('span')[3].get_text():
                    item['workYear'] = x.li.find_all('span')[3].get_text().encode('utf8')
                    item['education'] = x.li.find_all('span')[4].get_text().encode('utf8')
                else:
                    pass
            item['jobDes'] = x.li.li.get_text().encode('utf8')
            item['company'] = x.find_all('td',class_='gsmc')[0].get_text().encode('utf8')
            item['companySize'] = x.li.find_all('span')[2].get_text().encode('utf8')
            item['financeStage'] = x.li.find_all('span')[1].get_text().encode('utf8')
            item['industryField'] = ''
            #-------#
            item['rate'] = 0
            item['number'] = 0
            yield item


