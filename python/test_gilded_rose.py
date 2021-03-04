# -*- coding: utf-8 -*-
import unittest
import random
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Fake(self):
        items = [Item("fake", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fake", items[0].name)
    
    def test_Fake_Item_Quality_Standard(self):
        orginalQuality = 10
        sellInValue = 10
        items = [Item("foo",sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality-1)
        self.assertEqual(items[0].sell_in, sellInValue-1)

    def test_Fake_Item_Quality_PastSellIn(self):
        orginalQuality = 10
        sellInValue = -4
        items = [Item("foo",sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality-2)
        self.assertEqual(items[0].sell_in, sellInValue-1)
    
    def test_Fake_Item_Quality_NegativeTest(self):
        orginalQuality = 1
        sellInValue = -1
        items = [Item("foo",sellInValue, orginalQuality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, sellInValue-1)

    def test_AgedBrie_Quality(self):
        orginalQuality = 15
        items = [Item("Aged Brie",13,orginalQuality)]
        gilded_rose=GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(items[0].quality == orginalQuality+1 or items[0].quality == 50)
        self.assertEqual("Aged Brie", items[0].name)
        
    def test_Sulfuras_Quality(self):
        orginalQuality = 80
        items = [Item("Sulfuras",13,orginalQuality)]
        gilded_rose=GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, orginalQuality)
        self.assertEqual("Sulfuras", items[0].name)
    
    def test_BackStagePass_Quality_GreaterThan10DaysOut(self):
        items = [Item("fake", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fake", items[0].name)
    


if __name__ == '__main__':
    unittest.main()
