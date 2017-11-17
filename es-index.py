#!/usr/bin/env python

import json
import requests
from elasticsearch import Elasticsearch

# Textise to extract: https://www.textise.net
# Validate JSON with: https://jsonlint.com/
# Example: https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

data = json.load(open('articles.json'))

# Create a new index
es.indices.create(index='articles', ignore=400)

i = 1

# Add document (articles)
for a in data['articles']:
    # print a
    res = es.index(index='articles', doc_type='article', id=i, body=a)
    print "Indexed article: " + str(i)
    i += 1
