#!/bin/bash

docker run \
    -p 5141:5141 \
    -v ${PWD}/logstash/config:/usr/share/logstash/config \
    -v ${PWD}/logstash/pipeline:/usr/share/logstash/pipeline \
    -v ${PWD}/logstash/data:/usr/share/logstash/data \
docker.elastic.co/logstash/logstash:7.8.0
