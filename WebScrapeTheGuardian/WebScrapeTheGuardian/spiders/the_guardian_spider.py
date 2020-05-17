import scrapy
from ..items import WebscrapetheguardianItem
from datetime import date, timedelta,datetime


class The_Guardian_Spider(scrapy.Spider):
    name = 'theguardian'

    def start_requests(self):
        urls = [
            'https://www.theguardian.com/commentisfree/',
            'https://www.theguardian.com/world/',
            'https://www.theguardian.com/film/',
            'https://www.theguardian.com/games/',
            'https://www.theguardian.com/music/',
            'https://www.theguardian.com/lifeandstyle/',
            'https://www.theguardian.com/stage/',
            'https://www.theguardian.com/fashion/',
            'https://www.theguardian.com/business/',
            'https://www.theguardian.com/money/',
        ]

        for url in urls:
            url = self.formate_url(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('div.fc-container__body a.fc-item__link'):
            if link.attrib['data-link-name'] == 'article':
                yield scrapy.Request(url=link.attrib['href'], callback=self.parse_article)

    def parse_article(self, response):
        items = WebscrapetheguardianItem()
        items['title'] = response.css('h1::text').extract()
        items['series_label'] = response.css('.content__series-label .content__label__link span::text').extract()
        items['authors'] = response.xpath('//*[contains(@rel,"author")]//*/text() | //p[contains(@class,"byline")]//text()').extract()
        items['section_label'] = response.css('.content__section-label .content__label__link span::text').extract()
        items['article'] = response.xpath("//span[@class='css-14sgovv']/text() | //p[@class='css-h6rhrn']/text() | //a[@data-link-name='in body link']/text() | //*[contains(@class,'content__article-body')]//p//text()").extract()
        items['link'] = response.request.url
        yield items

    def formate_url(self,url):
        yasterday=date.today() - timedelta(days=1)
        day=yasterday.strftime("%d")
        mon=yasterday.strftime("%B")[:3]
        year=yasterday.strftime("%Y")
        return url+year+'/'+mon+'/'+day+'/all'
