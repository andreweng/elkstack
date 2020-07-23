#!/bin/bash

docker run -p 9200:9200 -p 9300:9300 -v ~/dock-es/elasticsearch/config:/usr/share/elasticsearch/config -v ~/dock-es/elasticsearch/logs:/usr/share/elasticsearch/logs -v ~/dock-es/elasticsearch/data:/usr/share/elasticsearch/data -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.8.0
