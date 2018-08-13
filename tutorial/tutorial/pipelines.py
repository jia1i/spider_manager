# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item


import json
import codecs

class JsonWithEncodingPipeline(object):
# class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    def process_item(self, item, spider):
        return item

    def spider_closed(self, spider):
        self.file.close()