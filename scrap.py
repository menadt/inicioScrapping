from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader


class Tema(Item):
    tema = Field()
    id = Field()

class taringaSpider(Spider):
    name= "probando Spider"
    start_urls = ["https://www.taringa.net/"]
    def parse(self, response):
        
