# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import date, timedelta
from rake_nltk import Rake
import re

class WebscrapetheguardianPipeline:
    def process_item(self, item, spider):

        item['date_article']=date.today() - timedelta(days=1) #add date article

        item['article']=self.article_cleanse(item['article']) #clean and generate article

        item['title'] = self.clean_string(item['title']) #cleaning Title

        item['series_label'] = self.clean_string(item['series_label'][0]) #cleaning series lines

        item['authors'] = self.authors_cleanse(self.Eliminate_trailing_lines_in_arr(item['authors'])) #cleaning authors

        item['section_label'] = self.Eliminate_trailing_lines_in_arr(item['section_label'])  #cleaning section label

        item['keywords']=self.generate_key_words(item['title'])+self.generate_key_words(item['article'],15) #generate keywords

        return item

    def clean_string(self,text):
        text = text.rstrip().lstrip()
        return re.sub('[^a-zA-Z0-9 \n\.]', '', text)

    def Eliminate_trailing_lines_in_arr(self,arr):
        return [self.clean_string(el) for el in arr]

    def authors_cleanse(self,authors):
        return [author for author in authors if len(author)>1 and author != 'and']

    def article_cleanse(self,article):
        return ''.join([self.clean_string(el) for el in article])

    def generate_key_words(self,text,nb_keywords=5,max_length=2):
        r = Rake(max_length=max_length)  # Uses stopwords for english from NLTK, and all puntuation characters.
        r.extract_keywords_from_text(text)
        keywords=r.get_ranked_phrases()
        return keywords[:min(nb_keywords,len(keywords))]   # return at most nb_keywords words with max length 2
