from flask import Blueprint

from .extensions import mongo
import json

main= Blueprint('main',__name__)

@main.route('/')
def index():
    TheGuardianScrap_articles_collection = mongo.db.articles
    all_articles=TheGuardianScrap_articles_collection.find()
    response = []
    for article in all_articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)
