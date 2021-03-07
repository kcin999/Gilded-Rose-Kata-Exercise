#include "GildedRose.h"

GildedRose::GildedRose(vector<Item> & items) : items(items)
{}
    
void GildedRose::updateQuality() 
{
    for (int i = 0; i < items.size(); i++)
    {
        updateOneItem(items[i]);
    }
}

void GildedRose::updateOneItem(Item& item) {
    if (item.name != "Aged Brie" && item.name != "Backstage passes to a TAFKAL80ETC concert")
    {
        if (item.name != "Sulfuras, Hand of Ragnaros")
        {
            decrementQuality(item);
        }
    }
    else
    {
        if (item.quality < 50)
        {
            item.quality = item.quality + 1;

            if (item.name == "Backstage passes to a TAFKAL80ETC concert")
            {
                if (item.sellIn < 11)
                {
                    incrementQuality(item);
                }

                if (item.sellIn < 6)
                {
                    incrementQuality(item);
                }
            }
        }
    }

    if (item.name != "Sulfuras, Hand of Ragnaros")
    {
        item.sellIn = item.sellIn - 1;
    }

    if (item.sellIn < 0)
    {
        if (item.name != "Aged Brie")
        {
            if (item.name != "Backstage passes to a TAFKAL80ETC concert")
            {
                if (item.name != "Sulfuras, Hand of Ragnaros")
                {
                    decrementQuality(item);
                }
            }
            else
            {
                item.quality = item.quality - item.quality;
            }
        }
        else
        {
            incrementQuality(item);
        }
    }

}

void GildedRose::decrementQuality(Item& item)
{
    if (item.quality > 0)
    {
        item.quality = item.quality - 1;
    }
}

void GildedRose::incrementQuality(Item& item)
{
    if (item.quality < 50)
    {
        item.quality = item.quality + 1;
    }
}
