import scrapy
import re
regex = re.compile(r'[\n\r\t]') #\f\s

class BlogSpider(scrapy.Spider):
    name = 'hagglerzspider'
    start_urls = ['https://salefinder.com.au/Woolworths-catalogue']

    def parse(self, response):
        # print(response.body)
        for item in response.css('.item-details-container'):
            yield {
                'item-name': regex.sub('', item.css('a.item-name ::text').get()),
                'price-options ': regex.sub('', item.css('div.price-options ::text').get()),
                'price': regex.sub('', item.css('span.price ::text').get()),
                'comparative-text': regex.sub('', item.css('span.comparative-text ::text').get())
                }

        # for next_page in response.css('a.pagenums'):
        #     yield response.follow(next_page, self.parse)