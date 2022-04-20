import scrapy
import logging

# Convert to understandable outputs
logging.getLogger('scrapy').setLevel(logging.WARNING)

# Define a Python class developed from scrapy.Spider

class Spider1(scrapy.Spider):
    name = "wikipedia"
    start_urls = ['https://en.wikipedia.org/wiki/Electric_battery']

    def parse(self, response):
        ''' To process the web page and find 
        what we want to extract from it. '''
        for e in response.css('div#mw-content-text>div>p'):
            yield { 'line' : ''.join(e.css('::text').getall()).strip() }