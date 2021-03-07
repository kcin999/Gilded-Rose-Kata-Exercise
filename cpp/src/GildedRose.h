#include <string>
#include <vector>

using namespace std;

class Item
{
public:
    string name;
    int sellIn;
    int quality;
    Item(string name, int sellIn, int quality) : name(name), sellIn(sellIn), quality(quality) 
    {}
};

class GildedRose
{
public:
    vector<Item> & items;
    GildedRose(vector<Item> & items);
    
    void updateQuality();
private:
    class ItemCategory {
    public:
        void updateOneItem(Item& item);
    protected:
        void decrementQuality(Item& item);
        void incrementQuality(Item& item);
        virtual void updateExpired(Item& item);
        virtual void updateSellIn(Item& item);
        virtual void updateQuality(Item& item);
    };
    class Legendary : public ItemCategory {
        void updateExpired(Item& item);
        void updateSellIn(Item& item);
        void updateQuality(Item& item);
    };

    class Cheese : public ItemCategory {
        void updateExpired(Item& item);
        void updateQuality(Item& item);
    };

    class BackstagePass :public ItemCategory {
        void updateExpired(Item& item);
        void updateQuality(Item& item);
    };

    class Conjured : public ItemCategory {
        void updateExpired(Item& item);
        void updateQuality(Item& item);
    };
};

