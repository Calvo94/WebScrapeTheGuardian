from flask import Blueprint

from .extensions import mongo
import json

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return f'<h1>Welcome to the guardian web scrapping API<h1>'


@main.route('/get_all', methods=['GET'])
def get_all_articles():
    TheGuardianScrap_articles_collection = mongo.db.articles
    all_articles = TheGuardianScrap_articles_collection.find()
    response = []
    for article in all_articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)


@main.route('/get_article_by_title/<title>', methods=['GET'])
def get_article_by_title(title):
    articles_collection = mongo.db.articles
    article = articles_collection.find_one({'title': title})

    response = {}
    for key, val in article.items():
        response[key] = val

    response['_id'] = str(response['_id'])

    return json.dumps(response)


@main.route('/get_author_articles/<author>', methods=['GET'])
def get_author_articles(author):
    articles_collection = mongo.db.articles
    articles = articles_collection.find({'authors': author})
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)


@main.route('/get_section_label_articles/<section_label>', methods=['GET'])
def get_section_label_articles(section_label):
    articles_collection = mongo.db.articles
    articles = articles_collection.find({'section_label': section_label})
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)


@main.route('/get_series_label_articles/<series_label>', methods=['GET'])
def get_series_label_articles(series_label):
    articles_collection = mongo.db.articles
    articles = articles_collection.find({'series_label': series_label})
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)


@main.route('/get_articles_by_keyword/<keywords>', methods=['GET'])
def get_articles_by_keywords(keywords):

    articles_collection = mongo.db.articles

    articles = articles_collection.find({'$text': {'$search': keywords}},
                                        {'score': {'$meta': "textScore"}}).sort([('textScore',-1)])
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)
