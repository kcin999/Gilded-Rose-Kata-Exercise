# -*- coding: utf-8 -*-
import unittest
import random
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Fake_Item_Quality_Standard(self):
        orginalQuality = 10
        sellInValue = 10
        name = "foo"
        items = [Item(name,sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality-1)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in, sellInValue-1)

    def test_Fake_Item_Quality_PastSellIn(self):
        orginalQuality = 10
        sellInValue = -4
        name = "foo"
        items = [Item(name,sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality-2)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in, sellInValue-1)
    
    def test_Fake_Item_Quality_NegativeTest(self):
        orginalQuality = 1
        sellInValue = -1
        name = "foo"
        items = [Item(name,sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in, sellInValue-1)

    def test_AgedBrie_Quality(self):
        orginalQuality = 15
        sellInValue = 13
        name = "Aged Brie"
        items = [Item(name,sellInValue ,orginalQuality)]
        gilded_rose=GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality,orginalQuality+1)
        self.assertEqual(name, items[0].name)
        self.assertEqual(items[0].sell_in,sellInValue-1)
        
    def test_AgedBrie_Quality_Over50(self):
        orginalQuality = 50
        sellInValue = 13
        name = "Aged Brie"
        items = [Item(name,sellInValue ,orginalQuality)]
        gilded_rose=GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality,50)
        self.assertEqual(name, items[0].name)
        self.assertEqual(items[0].sell_in,sellInValue-1)

    def test_Sulfuras_Quality(self):
        orginalQuality = 80
        sellInValue = 13
        name = "Sulfuras"
        items = [Item(name,sellInValue,orginalQuality)]
        gilded_rose=GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue)
    
    def test_BackStagePass_Quality_GreaterThan10DaysOut(self):
        orginalQuality = 20
        sellInValue = 15 
        name = "Backstage passes"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality+1)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)

    def test_BackStagePass_Quality_LessThan11DaysOut(self):
        orginalQuality = 20
        sellInValue = 10 
        name = "Backstage passes"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality+2)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)
    
    def test_BackStagePass_Quality_LessThan6DaysOut(self):
        orginalQuality = 20
        sellInValue = 5 
        name = "Backstage passes"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality+3)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)
    
    def test_BackStagePass_Quality_ConcertPast(self):
        orginalQuality = 20
        sellInValue = 0
        name = "Backstage passes"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)

    def test_Conjured_Item(self):
        orginalQuality = 20
        sellInValue = 15
        name = "Conjured Mana Cake"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality -2)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)

    def test_Conjured_Item_Negative_SellIn(self):
        orginalQuality = 1
        sellInValue = -1
        name = "Conjured Mana Cake"
        items = [Item(name, sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].name, name)
        self.assertEqual(items[0].sell_in,sellInValue-1)

if __name__ == '__main__':
    unittest.main()
