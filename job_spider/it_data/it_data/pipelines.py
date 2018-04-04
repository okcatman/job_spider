# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from models import *

class ItDataPipeline(object):
    def process_item(self, item, spider):
        session = Session()
        instance = Itdata(**item)
        session.merge(instance)
        session.commit()
        return item
