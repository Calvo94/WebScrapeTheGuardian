import scrapy
from ..items import WebscrapetheguardianItem

class The_Guardian_Spider(scrapy.Spider):
    name = 'theguardian'
    start_urls = [
        'https://www.theguardian.com/commentisfree/2020/may/15/all',
       # 'https://www.theguardian.com/commentisfree/2020/may/14/all',
     #   'https://www.theguardian.com/commentisfree/2020/may/13/all',
      #  'https://www.theguardian.com/commentisfree/2020/may/12/all',
    ]

    def parse(self, response):
        for link in response.css('div.fc-container__body a.fc-item__link'):
            if link.attrib['data-link-name'] == 'article':
                yield scrapy.Request(url=link.attrib['href'], callback=self.parse_article)

    def parse_article(self, response):

        items = WebscrapetheguardianItem()
        items['title'] = response.css('h1::text').extract()[0]
        items['series_label'] = response.css('.content__series-label .content__label__link span::text').extract()
        items['authors'] = response.xpath('//*[contains(@rel,"author")]//*/text() | //p[contains(@class,"byline")]//text()').extract()
        items['section_label'] = response.css('.content__section-label .content__label__link span::text').extract()
        items['article'] = response.xpath("//span[@class='css-14sgovv']/text() | //p[@class='css-h6rhrn']/text() | //a[@data-link-name='in body link']/text() | //*[contains(@class,'content__article-body')]//p//text()").extract()
        items['link'] = response.request.url

        yield items
