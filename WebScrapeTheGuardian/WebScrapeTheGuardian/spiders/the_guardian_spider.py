import scrapy


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

        title = response.css('h1::text').extract()[0].rstrip().lstrip()

        series_label = [el.rstrip().lstrip() for el in response.css('.content__series-label .content__label__link span::text').extract()]

        authors = response.css('.tone-colour span::text').extract()
        if len(authors) == 0:
            if 'Brief letters' in series_label :
                authors = ['Letter']
            else:
                authors = response.css('.byline::text').extract()

        section_label = [el.rstrip().lstrip() for el in response.css('.content__section-label .content__label__link span::text').extract()]

        yield {
            'title': title,
            'author': authors,
            'series_label': series_label,
            'section_label': section_label,
            'url': response.request.url
        }
