#!/usr/bin/env python

import json
import requests
from elasticsearch import Elasticsearch

# Textise to extract: https://www.textise.net
# Validate JSON with: https://jsonlint.com/
# Example: https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb

DEBUG = False

settings = json.load(open('settings.json'))
es = Elasticsearch([{'host': settings.hostname, 'port': settings.port}])

def display_articles(pages):
    for a in pages:
        print "Article: " + str(a['_id'] + " type: " + a['_type'])
        article = a['_source']
        print "\tWebsite: " + str(article['website'])
        print "\tAuthor: " + str(article['author'])
        print "\tTitle: " + str(article['title'])

        if DEBUG: print "ES Document: " + str(a)

doc = {
    'query': {
        'match_all' : {}
   }
}

chunk_size = 1

# Perform a scroll search (like a cursor) with page_size
page = es.search(index='articles', doc_type='article', body=doc, scroll='1m', size=chunk_size)
sid = page['_scroll_id']

current_page = 1
total = page['hits']['total']
page_size = page['hits']['total']
print "[- Query Overview -]"
print "\tPage Size: " + str(page_size)
print "\tScroll ID: " + sid
print "\tTime Taken: " + str(page['took'])
print "\tTimed Out: " + str(page['timed_out']) + "\n"

print "[ ---------------------------------------- ]\n"

# Process the first page and update if there are more
while page_size > 0:

    display_articles(page['hits']['hits'])

    page = es.scroll(scroll_id=sid, scroll = '1m')

    # Update scroll id and the length of the hits returned NOT the total
    # https://gist.github.com/drorata/146ce50807d16fd4a6aa
    sid = page['_scroll_id']
    page_size = len(page['hits']['hits'])
    print "\n[ - Page: " + (str(current_page)) + " of " + str(total) + " -]\n"
    current_page += 1

print "[ ---------------------------------------- ]\n"

es.clear_scroll(body={'scroll_id': [sid]}, ignore=(404))
