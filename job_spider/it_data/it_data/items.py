# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItDataItem(scrapy.Item):

    fromsite = scrapy.Field()             #源站点
    positionType = scrapy.Field()         #职位种类
    positionName = scrapy.Field()         #职位具体名字
    salary = scrapy.Field()               #薪水
    education = scrapy.Field()            #学历
    city = scrapy.Field()                 #地点
    workYear = scrapy.Field()             #工作经验
    jobDes = scrapy.Field()               #职位描述
    company = scrapy.Field()              #公司名
    companySize = scrapy.Field()          #公司规模
    financeStage = scrapy.Field()         #发展阶段
    industryField = scrapy.Field()        #所属领域
    #---------------------------------------------#
    rate = scrapy.Field()                 #星级
    number = scrapy.Field()               #招聘人数
