# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class CentauroPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## remove currency simbol
        field_name = 'price'
        value = adapter.get(field_name)
        value = value.replace('R$ ', '')
        adapter[field_name] = value

        ## set url
        field_name = 'url'
        link = 'https://www.centauro.com.br'
        value = adapter.get(field_name)
        value = link + value
        adapter[field_name] = value

        ## discount null
        field_name = 'discount'
        value = adapter.get(field_name)
        if not value:
            value = 0
        else:
            value = value.strip('-%')
        adapter[field_name] = int(value)

        return item
