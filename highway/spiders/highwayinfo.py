# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from highway.items import HighwayItem, StationItem


class HighwayinfoSpider(scrapy.Spider):
    name = 'highwayinfo'
    allowed_domains = ['shike.gaotie.cn']
    # start_urls = ['http://shike.gaotie.cn/checi.asp?checi=1152']

    def start_requests(self):
        file = open('rwcode.txt', 'r', encoding='utf8')
        # readlines读取返回列表
        urllist = file.readlines()
        start_urls = []
        for u in urllist:
            #格式化数据
            uri=u.strip()[1:-1]
            print(uri)
            yield scrapy.Request(url='http://shike.gaotie.cn/checi.asp?checi='+uri, callback=self.parse)


    def parse(self, response):
        '''
        解析html获取所需数据
        '''
        # 爬取下来的html代码
        html = response.text
        soup = BeautifulSoup(html, "html5lib")
        # 获取包裹所有数据的div
        div_b_all = soup.find('div', attrs={'align':'center'})
        # 实列化一个item
        item = HighwayItem()
        # 判断是否存在此盒子
        # （其实这里也可以不用加这个判断，因为它是肯定存在的，我这里加上去算是培养自己一个习惯吧，去获取的内容都进行判断，防止内容标签不存在而产生错误）
        if div_b_all is not None:
            #找到列车详情对应的table
            highwayInfoTable = div_b_all.find_all('table')[1]
            tr_arr = highwayInfoTable.find_all("tr")
            #遍历tr 放入列车详情数据
            for index, tr in enumerate(tr_arr):
                if index == 0:
                    item['name'] = tr.find_all('td')[2].find('strong').string
                    item['overTime'] = tr.find_all('td')[4].string
                elif index == 1:
                    item['startStation'] = tr.find_all('td')[1].string
                    item['endStation'] = tr.find_all('td')[3].string
                elif index == 2:
                    item['srartTime'] = tr.find_all('td')[1].string
                    item['endTime'] = tr.find_all('td')[3].string
                elif index == 3:
                    item['type'] = tr.find_all('td')[1].string
                    item['length'] = tr.find_all('td')[3].string

            #列车详情结束，，，开始解析各站点信息


            stationList = []
            stationTable = div_b_all.find_all('table')[3]
            tr_station = stationTable.find_all("tr")
            for index,tr in enumerate(tr_station):
                #除第一行表头外，每行为一个站点信息
                if index != 0 :
                    td_station=tr.find_all('td')
                    itemStation = StationItem()

                    itemStation['name'] = td_station[1].string
                    itemStation['inTime'] = td_station[2].string
                    itemStation['outTime'] = td_station[3].string
                    itemStation['stayTime'] = td_station[4].string
                    itemStation['dayNum'] = td_station[5].string
                    itemStation['overTime'] = td_station[6].string
                    itemStation['length'] = td_station[7].string
                    itemStation['seatNum'] = td_station[8].string.replace("\n", "")
                    itemStation['berthNum'] = td_station[9].string.replace("\n", "")
                    itemStation['sortBerthNum'] = td_station[10].string.replace("\n", "")

                    stationList.append(itemStation)

            item['stationList'] = stationList


            print(item)
            yield item

