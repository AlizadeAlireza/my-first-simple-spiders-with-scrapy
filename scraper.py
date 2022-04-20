import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "BrickSetSpider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            pass
