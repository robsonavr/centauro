import scrapy
from centauro.items import CentauroItem


class LuvasSpider(scrapy.Spider):
    name = "luvas"
    allowed_domains = ["www.centauro.com.br"]
    start_urls = ["https://www.centauro.com.br/busca/luva-de-goleiro"]

    def parse(self, response):
        luvas = response.css('a.ProductCard-styled__Card-sc-97c94e5e-0.gpfLHL')

        luva_item = CentauroItem()
        for luva in luvas:
            luva_item['description'] = luva.css('::attr(href)').get()
