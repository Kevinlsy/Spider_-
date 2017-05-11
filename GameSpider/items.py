# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class GamespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name = Field()
    game_pingtai = Field()
    game_kaifashang = Field()
    game_ticai = Field()
    game_yunyingshang = Field()
    game_moshi = Field()
    game_fufei = Field()
    game_leixing = Field()
