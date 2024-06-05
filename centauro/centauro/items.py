# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CentauroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    sku = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()

