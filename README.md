# Elasticsearch Experiments

Index stats: http://ec2-34-242-139-221.eu-west-1.compute.amazonaws.com/owen_articles/

Term vectors:
https://github.com/elastic/elasticsearch/issues/3114

## Basic search examples

* Word: { "match": { "address": "mill" } }
* Phrase: { "match_phrase": { "address": "mill lane" } }
* AND:

  "bool": {
    "must": [
      { "match": { "address": "mill" } },
      { "match": { "address": "lane" } }
    ]
  }

* OR: replace must with "should"
* NOT: replace must with "must_not"
* Can combine also bool expressions

## Using Filters

* Range for a numeric field:

  "filter": {
      "range": {
        "balance": {
          "gte": 20000,
          "lte": 30000
        }
      }
    }

## Aggregations

* Group by:

  {
    "size": 0,
    "aggs": {
      "group_by_state": {
        "terms": {
          "field": "state.keyword"
        }
      }
    }
  }

* Calculate average for a numeric field and order desc:

"aggs": {
  "group_by_state": {
    "terms": {
      "field": "state.keyword",
      "order": {
        "average_balance": "desc"
      }
    },
    "aggs": {
      "average_balance": {
        "avg": {
          "field": "balance"
        }
      }
    }
  }
}

* Last example here shows setting up groups and calculating averages for each group:

https://www.elastic.co/guide/en/elasticsearch/reference/current/_executing_aggregations.html

## Aggregations

* https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html
* avg
* cardinality
* extended stats
* geo bounds and geo centroid
* max and min
* percentiles, percentile ranks
* scripted metric
* sum
* top hits
* value count

## Queries

Query DSL: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html

* Full text
* Term level
* Compound
* Joining
* Geo
* Specialised
* Span
* Min should match
* Multi term query

## Mappings

These are specific types applied to an index when created

https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html

## Analysis

Process of converting text into tokens/terms added to inverted index for searching

## X Pack API's

* Graph
* Machine Learning - https://www.elastic.co/guide/en/elasticsearch/reference/current/ml-apis.html

# Text classification

https://www.elastic.co/blog/text-classification-made-easy-with-elasticsearch

n-gram modelling: https://sookocheff.com/post/nlp/n-gram-modeling/

n-gram tokenizer: https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-ngram-tokenizer.html

Sentiment Analysis: https://github.com/Jay-Wani/Elastic-twittersentiment-analysis

Topic Modelling:
