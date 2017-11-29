#!/usr/bin/env python

import json
import requests
from elasticsearch import Elasticsearch

# Textise to extract: https://www.textise.net
# Validate JSON with: https://jsonlint.com/
# Example: https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb

es = Elasticsearch([{'host': 'ec2-34-242-68-224.eu-west-1.compute.amazonaws.com', 'port': 9200}])

data = json.load(open('articles.json'))

# Create a new index
es.indices.delete(index='articles', ignore=[400,404])
