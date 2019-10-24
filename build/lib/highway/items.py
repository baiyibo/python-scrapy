# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HighwayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HighwayItem(scrapy.Item):
    #车次 G1876
    name = scrapy.Field()
    #运行时间
    overTime = scrapy.Field()
    #始发站
    startStation = scrapy.Field()
    #终点站
    endStation = scrapy.Field()
    #发车时间
    srartTime = scrapy.Field()
    # 到站时间
    endTime = scrapy.Field()
    #类型
    type = scrapy.Field()
    #全程
    length =scrapy.Field()

    #station数组
    stationList = scrapy.Field()

class StationItem(scrapy.Item):
    #站名
    name = scrapy.Field()
    # 到达时间
    inTime = scrapy.Field()
    # 离站时间
    outTime = scrapy.Field()
    # 停留时间
    stayTime = scrapy.Field()
    #天数
    dayNum = scrapy.Field()
    # 运行时间
    overTime = scrapy.Field()
    # 里程
    length = scrapy.Field()
    #硬座/软座
    seatNum = scrapy.Field()
    #硬卧上/中/下
    berthNum = scrapy.Field()
    # 软卧上/中/下
    sortBerthNum = scrapy.Field()