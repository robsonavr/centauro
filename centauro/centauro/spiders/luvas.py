import scrapy
from centauro.items import CentauroItem


class LuvasSpider(scrapy.Spider):
    name = "luvas"
    allowed_domains = ["www.centauro.com.br"]
    custom_settings = {
		'DOWNLOAD_DELAY': 10, # seconds of delay
        'RANDOMIZE_DOWNLOAD_DELAY': True
		}
    start_urls = ["https://www.centauro.com.br/busca/luva-de-goleiro"]

    def parse(self, response):
        luvas = response.css('a.ProductCard-styled__Card-sc-97c94e5e-0.gpfLHL')

        luva_item = CentauroItem()

        for luva in luvas:
            luva_item['url'] = luva.css('::attr(href)').get()
            luva_item['sku'] = luva.css('::attr(sku)').get()
            luva_item['description'] = luva.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-97c94e5e-3.hzAjfq::text').get()
            luva_item['price'] = luva.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.eFDcLB.Price-styled__CurrentPrice-sc-e083f0ed-4.etKnUk::text').get()
            luva_item['discount'] = luva.css('small.Typographystyled__Simple-sc-bdxvrr-5.lcUzEp.Price-styled__DiscountTag-sc-e083f0ed-6.loXLBV::text').get()

            yield luva_item


        for number_page in range(2,10):
            next_page = f'https://www.centauro.com.br/busca/luva-de-goleiro?page={number_page}'
            yield response.follow(next_page, callback=self.parse)
