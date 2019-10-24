# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exporters import JsonItemExporter
from  pymongo import MongoClient

from highway.items import HighwayItem


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


class MongodbPipeline(object):
    # 连接数据库
        def open_spider(self, spider):
            db_uri = spider.settings.get('MONGODB_URI', 'mongodb://host:port')
            db_name = spider.settings.get('MONGODB_DB_NAME', '所要连接数据库名称')
            self.db_client = MongoClient('mongodb://账户名:密码@host:port')
            self.db = self.db_client[db_name]
            # 关闭数据库

        def close_spider(self, spider):
            self.db_client.close()

        # 插入数据
        def process_item(self, item, spider):
            self.insert_db(item)

            return item

        def insert_db(self, item):
            if isinstance(item, HighwayItem):
                item = dict(item)  # 将一项数据转化为字典格式
            # 向集合artdb中插入数据
            self.db.artdb.insert_one(item)