#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "Catch.hpp"
#include "GildedRose.h"

TEST_CASE("GildedRoseUnitTest", "Foo")
{
    const string expected = "OMGHAI!\n"
            "-------- day 0 --------\n"
            "name, sellIn, quality\n"
            "+5 Dexterity Vest, 10, 20\n"
            "Aged Brie, 2, 0\n"
            "Elixir of the Mongoose, 5, 7\n"
            "Sulfuras, Hand of Ragnaros, 0, 80\n"
            "Sulfuras, Hand of Ragnaros, -1, 80\n"
            "Backstage passes to a TAFKAL80ETC concert, 15, 20\n"
            "Backstage passes to a TAFKAL80ETC concert, 10, 49\n"
            "Backstage passes to a TAFKAL80ETC concert, 5, 49\n"
            "Conjured Mana Cake, 3, 6\n"
            "\n"
            "-------- day 1 --------\n"
            "name, sellIn, quality\n"
            "+5 Dexterity Vest, 9, 19\n"
            "Aged Brie, 1, 1\n"
            "Elixir of the Mongoose, 4, 6\n"
            "Sulfuras, Hand of Ragnaros, 0, 80\n"
            "Sulfuras, Hand of Ragnaros, -1, 80\n"
            "Backstage passes to a TAFKAL80ETC concert, 14, 21\n"
            "Backstage passes to a TAFKAL80ETC concert, 9, 50\n"
            "Backstage passes to a TAFKAL80ETC concert, 4, 50\n"
            "Conjured Mana Cake, 2, 4\n" 
            "\n";

    cout << expected;
    vector<Item> items;

    items.emplace_back("+5 Dexterity Vest", 10, 20);
    items.emplace_back("Aged Brie", 2, 0);
    items.emplace_back("Elixir of the Mongoose", 5, 7);
    items.emplace_back("Sulfuras, Hand of Ragnaros", 0, 80);
    items.emplace_back("Sulfuras, Hand of Ragnaros", -1, 80);
    items.emplace_back("Backstage passes to a TAFKAL80ETC concert", 15, 20);
    items.emplace_back("Backstage passes to a TAFKAL80ETC concert", 10, 49);
    items.emplace_back("Backstage passes to a TAFKAL80ETC concert", 5, 49);

    // this Conjured item doesn't yet work properly
    items.emplace_back("Conjured Mana Cake", 3, 6);


    GildedRose app(items);

    std::string actual = "OMGHAI\n";

    for (int day = 0; day <= 1; day++)
    {
        actual += "-------- day " + std::to_string(day);
        actual += " --------\n";
        actual += "name, sellIn, quality\n";
        for (auto& item : items)
        {
            actual += item.name.c_str();
            actual += ", " +std::to_string(item.sellIn) + ", "+ std::to_string(item.quality) + "\n";
        }
        actual += ("\n");
        app.updateQuality();
    }
    cout << actual;

    REQUIRE(actual.compare(expected));
}
