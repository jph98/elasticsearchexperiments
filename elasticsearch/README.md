## Overview

* 10am first day
* 9am second day (finish at 3.30pm)

* MongoDB Text Indexing - https://docs.mongodb.com/manual/core/index-text/

## Concepts

https://www.elastic.co/guide/en/elasticsearch/reference/current/_basic_concepts.html

* Cluster - collection of nodes
* Node - single server with UUID
* Index - a collection of documents
* Document - single entity
* Shard - subdivision for storing on nodes
* Replication - ensures redundancy if a shard/node fails

## Use Cases

Qualitative Analysts - competitor analysis
* (monitoring competitor press releases)
* Keyword
* Sentiment Analysis/NLP
* Topic Modelling

Samples: articles

Automation:

Best Advice Systems - indie companies that assess products from insurers
* Give insurers ratings
* Guard methodology to produce scores
* Product Features to predict the links between these and the scores given

In-house: .NET, Java, JS Developers

## Architecture

Document per website
Document for all websites

## Tutorial

Start Elasticsearch: bin/elasticsearch
Install Sense: kibana-plugin install elastic/sense

Health Check:

  curl 'http://localhost:9200/?pretty'

Kibana
  http://localhost:5601/
