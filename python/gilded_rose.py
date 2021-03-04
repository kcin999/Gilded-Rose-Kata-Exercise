# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_aged_brie(self, item):
        if item.quality < 49:
            item.quality = item.quality +1
        item.sell_in = item.sell_in - 1

    def update_quality_backstage_passes(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = item.quality + 3
        elif item.sell_in <= 10:
            item.quality = item.quality + 2
        else:
            item.quality = item.quality + 1

        if item.quality > 50:
            item.quality = 50
        item.sell_in = item.sell_in - 1
    
    def update_quality_other_items(self, item):
        if item.sell_in < 0:
            item.quality = item.quality - 2
        else:
            item.quality = item.quality - 1
        
        if item.quality <0:
            item.quality = 0
        item.sell_in = item.sell_in- 1

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_quality_aged_brie(item)
            elif item.name == "Backstage passes":
                self.update_quality_backstage_passes(item)
            elif item.name != "Sulfuras":
                self.update_quality_other_items(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
