import scrapy
import logging

# Convert to understandable outputs
logging.getLogger('scrapy').setLevel(logging.WARNING)

# Define a Python class developed from scrapy.Spider

class Spider2(scrapy.Spider):
    name = "imdb"
    start_urls = ['http://www.imdb.com/chart/boxoffice']

    def parse(self, response):
        ''' To process the web page and find 
        what we want to extract from it. '''
        for e in response.css('div#boxoffice>table>body>tr'):
            yield {
                'title': ''.join(e.css('td.titleColumn>a::text').extract()).strip(),
                'weekend': ''.join(e.css('td.ratingColumn')[0].css('::text').extract()).strip(),
                'gross': ''.join(e.css('td.ratingColumn')[1].css('span.secondaryInfo::text').extract()).strip(),
                'weeks': ''.join(e.css('td.weeksColumn::text').extract()).strip(),
                'image': e.css('td.posterColumn img::attr(src)').extract_first(),
            }