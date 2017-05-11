# -*- coding: utf-8 -*-
import openpyxl

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
 # 游戏名称 操作平台 开发商 题材 运营商 模式 付费 类型
from items import GamespiderItem
class GamespiderPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(["游戏名称","操作平台","开发商","题材","运营商","模式","付费","类型"])

    def process_item(self, item, spider):
        if isinstance(item,GamespiderItem):
            line = [item["game_name"],item["game_pingtai"],item["game_kaifashang"] ,item["game_ticai"],item["game_yunyingshang"],item["game_moshi"] ,item["game_fufei"],item["game_leixing"]]
            self.sheet.append(line)

            self.wb.save("game_duan.xlsx")
        return item
