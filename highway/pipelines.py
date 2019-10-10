# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exporters import JsonItemExporter


class HighwayPipeline(object):
        def __init__(self):
            self.file = open('qsbk_1.json', 'wb')  # 必须二进制写入
            self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
            # 开始写入
            self.exporter.start_exporting()

        def open_spider(self, spider):
            print('爬虫开始')
            pass

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item

        def close_spider(self, spider):
            # 完成写入
            self.exporter.finish_exporting()
            self.file.close()
            pass
