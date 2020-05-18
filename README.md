# TheGuardianWebScraper

The web scrape project use the framework Scrapy, it give us as the ability to extract from the website the Guardian, and insert them in the mangodb database.

in this project I've used my server you can change it in the pipeline.py file

Requirement :
Scrapy , pymongo

In the development of the project I've assumed that the project will be lunched once a day to get yasterday's articles.

To lunch web scrapper follow these commandes :

cd WebScrapeTheGuardian
crapy crawl theguardian

# TheGuardianWebScraperAPI

The api use flask framework
to install it use the command :

pip install flask flask-pymongo python-dotenv

To lunch the API 
cd API_The_Guardian
flask run


in the api there's multiple routes :
  /get_all : to get all articles
  /get_article_by_title/<title> : to get article by title
  /get_author_articles/<author> : to get author's articles
  /get_section_label_articles/<section_label> : to get articles in the label section
  /get_series_label_articles/<series_label> : to get articles in the series label
  /get_articles_by_keyword/<keywords> : to get article by keyword
