#!/usr/bin/env python

import json
import requests
from elasticsearch import Elasticsearch

# Textise to extract: https://www.textise.net
# Validate JSON with: https://jsonlint.com/
# Example: https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb

es = Elasticsearch([{'host': 'ec2-34-242-68-224.eu-west-1.compute.amazonaws.com', 'port': 9200}])

data = json.load(open('articles.json'))

# https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html
settings = {
     "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "articles": {
            "properties": {
                "website": {
                    "type": "string"
                },
                "uri": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "author": {
                    "type": "string"
                },
                "content": {
                    "type": "text"
                },
            }
        }
     }
}

# Create a new index
es.indices.create(index='articles', ignore=400, body=settings)

i = 1

# Add document (articles)
for a in data['articles']:
    # print a
    res = es.index(index='articles', doc_type='article', id=i, body=a)
    print "Indexed article: " + str(i)
    i += 1
