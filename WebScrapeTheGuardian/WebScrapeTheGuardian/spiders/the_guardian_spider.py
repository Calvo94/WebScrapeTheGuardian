import scrapy

class The_Guardian_Spider(scrapy.Spider):
    name='theguardian'
    start_urls = [
        'https://www.theguardian.com/commentisfree/2020/may/15/all',
    ]
    def parse(self, response):
        for link in response.css('div.fc-container__body a.fc-item__link'):
            if link.attrib['data-link-name']=='article':
                yield {
                    'link':link.attrib['href'],
                    'type':link.attrib['data-link-name']
                }