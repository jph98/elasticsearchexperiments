#!/usr/bin/env python

import json
import requests
from elasticsearch import Elasticsearch
from textblob import TextBlob

# See http://dataconomy.com/2016/12/use-elasticsearch-nlp-text-mining
#
# Some things we can do:
# - Basic sentiment using
# - Measure TF-IDF (how important a word is)
# - Text Classification (run a MLTQ, aggregate hits by score) -
#   classify an article in terms of a category or sector (hairdresser, baker etc...)
#   More accurate - train an SVM model or use Naiive Bayes
# - Language Detection (with plugin)
#
# Textblob can perform a lot of different analysis using NLTK
# http://textblob.readthedocs.io/en/dev/quickstart.html#quickstart
#
def display_sentiment(pages):
    for p in pages:
        a = p["_source"]
        blob = TextBlob(a["content"])
        print blob.sentiment

settings = json.load(open('settings.json'))
print 'Using ' + settings['hostname'] + ' ' + str(settings['port'])
es = Elasticsearch([{'host': settings['hostname'], 'port': settings['port']}])

doc = {
    'query': {
        'match_all' : {}
   }
}

chunk_size = 1
page = es.search(index='articles', doc_type='article', body=doc, scroll='1m', size=chunk_size)
sid = page['_scroll_id']
current_page = 1
total = page['hits']['total']
page_size = page['hits']['total']

while page_size > 0:
    display_sentiment(page['hits']['hits'])
    page = es.scroll(scroll_id=sid, scroll = '1m')
    sid = page['_scroll_id']
    page_size = len(page['hits']['hits'])
    current_page += 1

es.clear_scroll(body={'scroll_id': [sid]}, ignore=(404))
