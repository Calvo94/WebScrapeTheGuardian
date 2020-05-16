import scrapy
from ..items import WebscrapetheguardianItem

class The_Guardian_Spider(scrapy.Spider):
    name = 'theguardian'
    start_urls = [
        'https://www.theguardian.com/commentisfree/2020/may/15/all',
        'https://www.theguardian.com/commentisfree/2020/may/14/all',
        'https://www.theguardian.com/commentisfree/2020/may/13/all',
        'https://www.theguardian.com/commentisfree/2020/may/12/all',
    ]

    def parse(self, response):
        for link in response.css('div.fc-container__body a.fc-item__link'):
            if link.attrib['data-link-name'] == 'article':
                yield scrapy.Request(url=link.attrib['href'], callback=self.parse_article)

    def parse_article(self, response):

        items = WebscrapetheguardianItem()

        items['title'] = response.css('h1::text').extract()[0].rstrip().lstrip()

        series_label = [el.rstrip().lstrip() for el in response.css('.content__series-label .content__label__link span::text').extract()]

        authors = response.xpath('//*[contains(@rel,"author")]//*/text()').extract()

        if len(authors) == 0:
            if 'Brief letters' in series_label :
                authors = ['Letter']
            else:
                authors = response.css('.byline::text').extract()
        items['series_label']=series_label
        items['authors']=authors
        items['section_label'] = [el.rstrip().lstrip() for el in response.css('.content__section-label .content__label__link span::text').extract()]

        items['article'] = ''.join(response.xpath("//span[@class='css-14sgovv']/text() | //p[@class='css-h6rhrn']/text() | //a[@data-link-name='in body link']/text() | //*[contains(@class,'content__article-body')]//p//text()").extract())
        items['link'] = response.request.url
        yield items
