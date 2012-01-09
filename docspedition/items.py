# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DocspeditionItem(Item):
    name = Field()
    link = Field()
    description = Field()
