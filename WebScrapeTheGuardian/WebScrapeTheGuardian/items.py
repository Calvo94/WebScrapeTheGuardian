# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapetheguardianItem(scrapy.Item):
    # define the fields for your item here like:

    date_article = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    series_label = scrapy.Field()
    section_label = scrapy.Field()
    link = scrapy.Field()
    article = scrapy.Field()

