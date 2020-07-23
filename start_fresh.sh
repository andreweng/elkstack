#!/bin/bash

rm -fr elasticsearch/data/* &&
rm -fr elasticsearch/logs/* &&
rm -fr kibana/data/* &&
rm -fr logstash/data/* &&
echo "Elasticsearch, Kibana, and Logstash data purged!"
