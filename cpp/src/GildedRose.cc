#include "GildedRose.h"

GildedRose::GildedRose(vector<Item> & items) : items(items)
{}
    
void GildedRose::updateQuality() 
{
    for (int i = 0; i < items.size(); i++)
    {
        if (items[i].name.compare("Sulfuras, Hand of Ragnaros") == 0) {
            Legendary category = Legendary();
            category.updateOneItem(items[i]);
        }
        else if (items[i].name.compare("Aged Brie") == 0) {
            Cheese category = Cheese();
            category.updateOneItem(items[i]);
        }
        else if (items[i].name.compare("Backstage passes to a TAFKAL80ETC concert")==0) {
            BackstagePass category = BackstagePass();
            category.updateOneItem(items[i]);
        }
        else
        {
            ItemCategory category = ItemCategory();
            category.updateOneItem(items[i]);
        }
    }
}

void GildedRose::ItemCategory::updateOneItem(Item& item) {
    updateQuality(item);

    updateSellIn(item);

    if (item.sellIn < 0) {
        updateExpired(item);
    }
    
}

void GildedRose::ItemCategory::updateQuality(Item& item) {
    decrementQuality(item);
}

void GildedRose::ItemCategory::updateSellIn(Item& item) {
    item.sellIn = item.sellIn - 1;
}

void GildedRose::ItemCategory::updateExpired(Item& item) {
    decrementQuality(item);
}

void GildedRose::ItemCategory::decrementQuality(Item& item)
{
    if (item.quality > 0)
    {
        item.quality = item.quality - 1;
    }
}

void GildedRose::ItemCategory::incrementQuality(Item& item)
{
    if (item.quality < 50)
    {
        item.quality = item.quality + 1;
    }
}

void GildedRose::Legendary::updateExpired(Item& item) {};

void GildedRose::Legendary::updateSellIn(Item& item) {};

void GildedRose::Legendary::updateQuality(Item& item) {};

void GildedRose::Cheese::updateExpired(Item& item){
    incrementQuality(item);
};

void GildedRose::Cheese::updateQuality(Item& item) {
    incrementQuality(item);
};

void GildedRose::BackstagePass::updateQuality(Item& item) {
    incrementQuality(item);

    if (item.sellIn <= 10) {
        incrementQuality(item);
    }
    if (item.sellIn <= 5) {
        incrementQuality(item);
    }
}

void GildedRose::BackstagePass::updateExpired(Item& item) {
    item.quality = 0;
}