#-*- coding:utf-8 -*-
#game_duan为主程序，在S

import scrapy
from scrapy import Selector
from scrapy import Request
from GameSpider.items import GamespiderItem

class Spider(scrapy.Spider):


    name = "Spider"
    host = "http://newgame.17173.com/"
    start_urls = ["http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-3-2.html",
                  "http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-3-2.html"]



    def parse_list(self, response):
        selector =Selector(response)
        content_list = selector.xpath('//a[@class="avatar "]')
        for content in content_list:
            url = content.xpath("@href").extract_first()
            # print url
            yield Request(url=url,callback=self.parse_game)

    def parse_game(self,response):
        selector = Selector(response)
        #游戏名称
        game_name = selector.xpath('//h1[@class="tit"]/text()').extract_first()
        print game_name
        #操作平台
        game_pingtai = selector.xpath('//a[@title="PC"]/text()').extract_first()
        # print game_pingtai
        # #画风
        # game_huafeng = selector.xpath('//a[@title="Q版"]/text()').extract_first()
        # rint game_huafeng
        #开发商
        game_kaifashang = selector.xpath('//ul[@class="list-mater-info"]/li[position()=4]/a/text()').extract_first()
        # print game_kaifashang
        #题材
        game_ticai = selector.xpath('//ul[@class="list-mater-info"]/li[position()=5]/a/text()').extract_first()
        # print game_ticai
        #运营商
        game_yunyingshang = selector.xpath('//ul[@class="list-mater-info"]/li[position()=6]/span[position()=2]/a/text()').extract_first()
        # print game_yunyingshang
        #模式
        game_moshi = selector.xpath('//ul[@class="list-mater-info"]/li[position()=7]/a/text()').extract_first()
        # print game_moshi
        #付费
        game_fufei = selector.xpath('//ul[@class="list-mater-info"]/li[position()=8]/span[position()=2]/text()').extract_first()
        # print game_fufei
        #类型
        game_leixing = selector.xpath('//ul[@class="list-mater-info"]/li[position()=9]/a/text()').extract_first()
        # print game_leixing

        item = GamespiderItem()
        item["game_name"] = game_name
        item["game_pingtai"] = game_pingtai
        item["game_kaifashang"] = game_kaifashang
        item["game_ticai"] = game_ticai
        item["game_yunyingshang"] = game_yunyingshang
        item["game_moshi"] = game_moshi
        item["game_fufei"] =game_fufei
        item["game_leixing"] = game_leixing

        yield item

    # def parsr_page(self,response):
    #     selector = Selector(response)
    #     self.parse_list(response)
    #     url = selector.xpath('//div[@class="pagination"]/li[position()=3]/text()').extract_first()
    #     yield Request(url=url,callback=self.parsr_page())

    def start_requests(self):
        i = 0
        for url in self.start_urls:
            i +=1
            if i == 1:
                yield Request(url=url,callback=self.parse_list)
            if i == 2:
                for j in range(2,127):
                    yield Request(url=url+"?page={}".format(j), callback=self.parse_list)